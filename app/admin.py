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

admin.site.register(Bypass)
admin.site.register(Tipuri)
admin.site.register(MotiveBypass)
admin.site.register(Transportatori)
admin.site.register(Soferi)
admin.site.register(Cisterne)
admin.site.register(TipStatie)
admin.site.register(Client)
admin.site.register(Particular)
admin.site.register(Depozit)
admin.site.register(Test)
admin.site.register(Statie)
