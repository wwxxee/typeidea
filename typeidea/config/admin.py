from django.contrib import admin

from .models import Link, SideBar
from typeidea.custom_site import custom_site
# Register your models here.


@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'href', 'status', 'weight', 'ower', 'create_time',
    )
    fields = (
        'title', 'href', 'status', 'weight',
    )

    def save_model(self, request, obj, form, change):
        obj.ower = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'display_type', 'content', 'ower', 'create_time'
    )
    fields = (
        'title', 'display_type', 'status', 'content',
    )

    def save_model(self, request, obj, form, change):
        obj.ower = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
