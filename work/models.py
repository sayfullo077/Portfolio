from django.db import models
from common.models import Media


class Experience(models.Model):
    WORK = "work"
    EDUCATION = "education"
    TYPE_CHOICES = [(WORK, "Work"), (EDUCATION, "Education")]

    exp_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=WORK)
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} at {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ForeignKey(
        Media, on_delete=models.SET_NULL, null=True, blank=True, related_name="project_images"
    )
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]

    def __str__(self):
        return self.title


class Service(models.Model):
    ICON_CHOICES = [
        # Dasturlash
        ("code-slash-outline",        "💻 Kod / Dasturlash"),
        ("terminal-outline",          "🖥️ Terminal / Backend"),
        ("server-outline",            "🗄️ Server / API"),
        ("layers-outline",            "📦 Full-stack"),
        # Web
        ("globe-outline",             "🌐 Web sayt"),
        ("browsers-outline",          "🪟 Frontend"),
        ("desktop-outline",           "🖥 Desktop"),
        # Mobil
        ("phone-portrait-outline",    "📱 Mobil ilova"),
        ("logo-android",              "🤖 Android"),
        ("logo-apple",                "🍎 iOS"),
        # Ijtimoiy / Bot
        ("paper-plane-outline",       "✈️ Telegram bot"),
        ("chatbubbles-outline",       "💬 Chat-bot"),
        ("logo-discord",              "🎮 Discord bot"),
        # Dizayn
        ("color-palette-outline",     "🎨 UI/UX Dizayn"),
        ("brush-outline",             "🖌️ Grafik dizayn"),
        ("image-outline",             "🖼️ Banner / Rasm"),
        # Marketing / SEO
        ("trending-up-outline",       "📈 SEO / Marketing"),
        ("megaphone-outline",         "📣 Reklama"),
        ("bar-chart-outline",         "📊 Analitika"),
        # Boshqa
        ("construct-outline",         "🔧 Texnik yordam"),
        ("shield-checkmark-outline",  "🛡️ Xavfsizlik"),
        ("cloud-upload-outline",      "☁️ Hosting / Deploy"),
        ("settings-outline",          "⚙️ Avtolashtirish"),
        ("camera-outline",            "📷 Foto/Video"),
        ("musical-notes-outline",     "🎵 Musiqa / Audio"),
        ("school-outline",            "🎓 Ta'lim / Kurs"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to="services/", blank=True)
    icon_name = models.CharField(
        max_length=60, blank=True,
        choices=ICON_CHOICES,
        help_text="Xizmat uchun ikonka tanlang"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    level = models.PositiveIntegerField(default=0)
    icon = models.ImageField(upload_to="skills/", blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
