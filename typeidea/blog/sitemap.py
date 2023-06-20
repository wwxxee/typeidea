from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PostSitemap(Sitemap):
    changefreg = "always"
    priority = 1.0
    protocol = 'https'

    def items(self):
        """
        返回所有正常状态的文章
        :return:
        """
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        """
        返回每篇文章的创建时间，或者最近更新时间
        :param obj:
        :return:
        """
        return obj.create_time

    def location(self, obj):
        """
        返回每篇文章的url
        :param obj:
        :return:
        """
        return reverse('post-detail', args=[obj.pk])
