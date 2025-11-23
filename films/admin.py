from django.contrib import admin
from .models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'review')
    list_filter = ('title',)
    search_fields = ('title', 'description')
