from django.contrib import admin


class BaseOwerAdmin(object):
    """
    1.用来自动补充文章，分类，标签，侧边栏，友链这些model的ower字段
    2.用来针对queryset过来当前用户的数据
    即抽取 save_model() 和 get_queryset()方法
    """
    exclude = ['ower']

    """
    自定义数据列表页，实现让当前用户在列表页中只能看到自己创建的数据
    """
    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        return qs.filter(ower=request.user)

    def save_models(self):
        self.new_obj.ower = self.request.user
        return super().save_models()
