from django.contrib import admin
from django.utils.html import format_html
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'link', 'image_tag')
    readonly_fields = ('image_tag',)
    search_fields = ('title',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:80px;" />', obj.image.url)
        return ''
    image_tag.short_description = 'Image'

admin.site.register(Project, ProjectAdmin)
