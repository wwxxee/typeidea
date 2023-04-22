from django.contrib import admin

from .models import Link, SideBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwerAdmin
# Register your models here.


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwerAdmin):
    list_display = (
        'title', 'href', 'status', 'weight', 'ower', 'create_time',
    )
    fields = (
        'title', 'href', 'status', 'weight',
    )


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwerAdmin):
    list_display = (
        'title', 'display_type', 'content', 'ower', 'create_time'
    )
    fields = (
        'title', 'display_type', 'status', 'content',
    )

