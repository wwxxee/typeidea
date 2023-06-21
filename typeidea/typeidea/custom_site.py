from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_title = 'JoWon 管理后台'  # 标签页
    site_header = 'JoWon'  # 功能条
    index_title = '首页'  # 内容第一行


custom_site = CustomSite(name='cus_admin')
