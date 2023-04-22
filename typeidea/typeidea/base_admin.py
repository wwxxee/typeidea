from django.contrib import admin


class BaseOwerAdmin(admin.ModelAdmin):
    """
    1.用来自动补充文章，分类，标签，侧边栏，友链这些model的ower字段
    2.用来针对queryset过来当前用户的数据
    即抽取 save_model() 和 get_queryset()方法
    """
    exclude = ['ower']

    """
    自定义数据列表页，实现让当前用户在列表页中只能看到自己创建的数据
    """
    def get_queryset(self, request):
        qs = super(BaseOwerAdmin, self).get_queryset(request)
        return qs.filter(ower=request.user)

    def save_model(self, request, obj, form, change):
        obj.ower = request.user
        return super(BaseOwerAdmin, self).save_model(request, obj, form, change)
