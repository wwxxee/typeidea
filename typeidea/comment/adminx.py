from django.contrib import admin
import xadmin
from .models import Comment
from typeidea.custom_site import custom_site

# Register your models here.


@xadmin.sites.register(Comment)
class CommentAdmin(object):
    list_display = (
        'target', 'nickname', 'content', 'website', 'email', 'create_time',
    )



