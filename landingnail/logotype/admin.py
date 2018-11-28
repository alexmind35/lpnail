from django.contrib import admin
from.models import Logo

@admin.register(Logo)
class AdminLogo(admin.ModelAdmin):
    list_display = ["logoimg"]
