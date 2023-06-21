from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwerAdmin
import xadmin
from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter
# Register your models here.


# class PostInline:
#     form_layout = (
#         Container(
#             Row("title", "desc"),
#         )
#     )
#     extra = 1  # 控制额外多几个
#     model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwerAdmin):
    list_display = ('id', 'name', 'status', 'is_nav', 'ower', 'post_count', 'create_time')
    fields = ('name', 'status', 'is_nav')

    # 在分类管理中添加inliens属性
    # inlines = [PostInline, ]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwerAdmin):
    list_display = ('name', 'status', 'ower', 'create_time')
    fields = ('name', 'status')


class CategoryOwerFilter(RelatedFieldListFilter):
    """
    自定义过滤器只展示当前用户的分类
    """
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super(CategoryOwerFilter, self).__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Category.objects.filter(ower=request.user).values_list('id', 'name')


# class TagOwerFilter(RelatedFieldListFilter):#  定义标签过滤器，不起作用
#     @classmethod
#     def test(cls, field, request, params, model, admin_view, field_path):
#         return field.name == 'tag'
#
#     def __init__(self, field, request, params, model, model_admin, field_path):
#         super().__init__(field, request, params, model, model_admin, field_path)
#         self.lookup_choices = Tag.objects.filter(ower=request.user).values_list('id', 'name')


manager.register(CategoryOwerFilter, take_priority=True)
# manager.register(TagOwerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwerAdmin):

    form = PostAdminForm

    list_display = [
        'id', 'title', 'category', 'status', 'ower',
        'create_time', 'operator'
    ]

    # 指定哪些字段不展示,list_display比这个优先级高
    # exclude = ['ower']

    # 用来配置哪些字段可以作为链接点击，点击可以进入编辑界面，默认第一个可以点击
    list_display_links = []

    list_filter = ['category']
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    """
    用filedsets替换fields，fieldsset用来控制布局。
    fieldsets = (
        (名称，{内容})，
        (名称，{内容})，
    )
    第一个元素是string（当前板块的名称），第二个元素是dict（当前板块的描述，字段和样式配置）
    dict的key可以是'fields', 'description', 'classes'
    """
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )
    # fieldsets = (
    #     ('基础配置', {
    #         'description': '基础配置描述',
    #         'fields': (
    #             ('title', 'category'),
    #             'status',
    #         ),
    #     }),
    #     ('内容', {
    #         'fields': (
    #             'desc',
    #             'content',
    #         ),
    #     }),
    #     ('额外信息', {
    #         'classes': ('wide', ),
    #         'fields': ('tag', )
    #     })
    # )

    # 针对多对多字段的展示配置
    filter_horizontal = ('tag', )
    # filter_vertical = ('tag',)

    # 展示自定义字段
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
        )

    # 指定展示文案
    operator.short_description = '操作'

    # class Media:
    #     """
    #     通过自定义Media类来往页面上添加JavaScript和css资源
    #     """
    #     css = {
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )
