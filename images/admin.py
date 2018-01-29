from django.contrib import admin
from .models import Image, Comment, Like
# Register your models here.
class ImageAdmin(admin.ModelAdmin):

    ordering = (
        'caption',
        'created_at'
    )

    list_display = (
        'location',
        'caption',
        'created_by',
        'updated_at',
        'created_at'
    )

    list_display_links = ('caption',)

    search_fields = (
        'location',
    )

    list_filter = (
        'created_at',
        'location'
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
admin.site.register(Like)