from django.contrib import admin

from .models import (
    Bypass,
    Cisterne,
    Client,
    Depozit,
    MotiveBypass,
    Particular,
    Soferi,
    Statie,
    Test,
    TipStatie,
    Tipuri,
    Transportatori,
)


@admin.register(Bypass)
class BypassAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "motiv",
        "sofer",
        "transportator",
        "cisterna",
        "tip_statie",
        "utilizator",
        "created_at",
    )
    list_filter = ("motiv", "tip", "tip_statie", "transportator", "created_at")
    search_fields = (
        "sofer__nume",
        "transportator__nume",
        "cisterna__nr_cisterna",
        "observatii",
        "utilizator__username",
    )
    date_hierarchy = "created_at"


@admin.register(Tipuri)
class TipuriAdmin(admin.ModelAdmin):
    search_fields = ("tip",)


@admin.register(MotiveBypass)
class MotiveBypassAdmin(admin.ModelAdmin):
    search_fields = ("motiv",)


@admin.register(Transportatori)
class TransportatoriAdmin(admin.ModelAdmin):
    search_fields = ("nume",)


@admin.register(Soferi)
class SoferiAdmin(admin.ModelAdmin):
    list_display = ("nume", "companie")
    list_filter = ("companie",)
    search_fields = ("nume", "companie__nume")


@admin.register(Cisterne)
class CisterneAdmin(admin.ModelAdmin):
    list_display = ("nr_cisterna", "companie")
    list_filter = ("companie",)
    search_fields = ("nr_cisterna", "companie__nume")


@admin.register(TipStatie)
class TipStatieAdmin(admin.ModelAdmin):
    search_fields = ("tip_statie",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ("nume",)


@admin.register(Particular)
class ParticularAdmin(admin.ModelAdmin):
    search_fields = ("nume",)


@admin.register(Depozit)
class DepozitAdmin(admin.ModelAdmin):
    search_fields = ("nume",)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    search_fields = ("nume",)


@admin.register(Statie)
class StatieAdmin(admin.ModelAdmin):
    list_display = ("nume", "tip_statie", "cod_statie")
    list_filter = ("tip_statie",)
    search_fields = ("nume", "cod_statie", "info_statie")
