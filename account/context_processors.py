from .models import User as PortfolioUser


def get_site_owner(request):
    try:
        owner = PortfolioUser.objects.first()
    except Exception:
        owner = None
    return {"site_owner": owner}
