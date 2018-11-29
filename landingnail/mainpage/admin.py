from django.contrib import admin

from.models import About

@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display = ["name","privet", "description","photo"]
