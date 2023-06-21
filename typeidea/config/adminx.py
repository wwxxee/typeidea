from django.contrib import admin
import xadmin
from .models import Link, SideBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwerAdmin
# Register your models here.


@xadmin.sites.register(Link)
class LinkAdmin(BaseOwerAdmin):
    list_display = (
        'title', 'href', 'status', 'weight', 'ower', 'create_time',
    )
    fields = (
        'title', 'href', 'status', 'weight',
    )


@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwerAdmin):
    list_display = (
        'title', 'display_type', 'content', 'ower', 'create_time'
    )
    fields = (
        'title', 'display_type', 'status', 'content',
    )

