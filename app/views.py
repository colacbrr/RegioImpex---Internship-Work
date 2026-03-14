import csv

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BypassForm
from .models import Bypass


@login_required
def bypass(request):
    if request.method == "POST":
        form = BypassForm(request.POST)
        if form.is_valid():
            bypass = form.save(commit=False)
            bypass.utilizator = request.user
            bypass.save()
            messages.success(request, "Bypass entry created successfully.")
            return redirect("bypass")
    else:
        form = BypassForm()

    return render(request, "formular_bypass.html", {"form": form})


@login_required
def bypass_list(request):
    query = request.GET.get("q", "").strip()
    bypass_entries = Bypass.objects.select_related(
        "motiv",
        "sofer",
        "transportator",
        "cisterna",
        "tip",
        "tip_statie",
        "utilizator",
    )

    if query:
        bypass_entries = bypass_entries.filter(
            Q(motiv__motiv__icontains=query)
            | Q(sofer__nume__icontains=query)
            | Q(transportator__nume__icontains=query)
            | Q(cisterna__nr_cisterna__icontains=query)
            | Q(observatii__icontains=query)
            | Q(utilizator__username__icontains=query)
        )

    paginator = Paginator(bypass_entries, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "bypass_list.html",
        {
            "page_obj": page_obj,
            "query": query,
            "result_count": paginator.count,
        },
    )


@login_required
def export_bypass_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="bypass-entries.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            "Created at",
            "Reason",
            "Driver",
            "Transport company",
            "Tanker",
            "Type",
            "Station type",
            "Created by",
            "Notes",
        ]
    )

    for entry in Bypass.objects.select_related(
        "motiv",
        "sofer",
        "transportator",
        "cisterna",
        "tip",
        "tip_statie",
        "utilizator",
    ):
        writer.writerow(
            [
                entry.created_at.isoformat(timespec="minutes"),
                entry.motiv,
                entry.sofer,
                entry.transportator,
                entry.cisterna,
                entry.tip,
                entry.tip_statie,
                entry.utilizator.username,
                entry.observatii,
            ]
        )

    return response
