from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

from work.models import Project, Skill, Experience, Service
from blog.models import Post
from .models import Contact


def home(request):
    return render(request, "home.html", {
        "featured_projects": Project.objects.filter(is_featured=True)[:3],
        "services": Service.objects.all(),
        "recent_posts": Post.objects.filter(is_published=True).order_by("-created_at")[:3],
    })


def about(request):
    return render(request, "about.html", {
        "work_experiences": Experience.objects.filter(exp_type=Experience.WORK),
        "education": Experience.objects.filter(exp_type=Experience.EDUCATION),
        "skills": Skill.objects.all(),
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        if settings.EMAIL_HOST_USER:
            body = (
                f"Yangi xabar keldi!\n\n"
                f"Ism: {name}\n"
                f"Email: {email}\n"
                f"Mavzu: {subject}\n\n"
                f"Xabar:\n{message}\n\n"
                f"---\n"
                f"Bu xabar portfolio saytidagi Contact formadan yuborildi."
            )
            try:
                EmailMessage(
                    subject=f"[Portfolio] {subject or 'Yangi xabar'} — {name}",
                    body=body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[email],
                ).send(fail_silently=False)
            except Exception:
                pass

        messages.success(request, "Xabaringiz yuborildi! Tez orada javob beraman.")
        return redirect("contact")
    return render(request, "contact.html")
