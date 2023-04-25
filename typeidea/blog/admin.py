from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwerAdmin

# Register your models here.


class PostInline(admin.TabularInline):  # StackedInline样式不同
    """
    可以在分类页面直接边界文章，即在同一页面关联数据，在分类页面关联文章数据
    内置编辑（伪需求，示例）
    """
    fields = ('title', 'desc')
    extra = 1  # 同时控制额外多几个
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwerAdmin):
    list_display = ('id', 'name', 'status', 'is_nav', 'ower', 'post_count', 'create_time')
    fields = ('name', 'status', 'is_nav')

    # 在分类管理中添加inliens属性
    inlines = [PostInline, ]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwerAdmin):
    list_display = ('name', 'status', 'ower', 'create_time')
    fields = ('name', 'status')


class CategoryOwerFilter(admin.SimpleListFilter):
    """
    自定义过滤器只展示当前用户的分类
    """

    title = '分类过滤器'
    parameter_name = 'ower_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(ower=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
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

    list_filter = [CategoryOwerFilter]
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

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide', ),
            'fields': ('tag', )
        })
    )

    # 针对多对多字段的展示配置
    filter_horizontal = ('tag', )
    # filter_vertical = ('tag',)

    # 展示自定义字段
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    # 指定展示文案
    operator.short_description = '操作'

    class Media:
        """
        通过自定义Media类来往页面上添加JavaScript和css资源
        """
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'object_repr', 'object_id', 'action_flag', 'user', 'change_message'
    ]
