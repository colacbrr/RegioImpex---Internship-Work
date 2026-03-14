from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import Bypass
from users.views import is_admin


@login_required
def root_view(request, *args, **kwargs):
    recent_entries = Bypass.objects.select_related(
        "motiv",
        "transportator",
        "utilizator",
    )[:5]
    context = {
        "metrics": {
            "total_bypass_entries": Bypass.objects.count(),
            "entries_this_user": Bypass.objects.filter(utilizator=request.user).count(),
            "total_users": (
                request.user.__class__.objects.count()
                if is_admin(request.user)
                else None
            ),
        },
        "recent_entries": recent_entries,
        "can_manage_users": is_admin(request.user),
    }
    return render(request, "root.html", context)


def error_404_view(request, exception):
    return render(request, "404.html", status=404)


def error_500_view(request):
    return render(request, "500.html", status=500)
