

import xadmin
from .models import Aiscore
from xadmin import views

# class BlogAdmin(object):
#   # 设置后台展示字段
#     list_display = ['name', 'desc', 'detail']
#     # 设置后台搜索字段 # 注意搜索字段不能有时间类型，否则会报错
#     search_fields = ['name']
#     # 设置后台过滤筛选字段，时间字段可以用过滤字段
#     list_filter = ['name']


class AiscoreAdmin(object):
    list_display = ['title', 'partner', 'describe', "createdate"]
    search_fields = ['title']
    list_filter = ['title']
    # style_fields = {"detail": "ueditor"}


xadmin.site.register(Aiscore, AiscoreAdmin)



class BaseSettings(object):
    enable_themes = True   # 使用主题功能
    use_bootswatch = True
    
xadmin.site.register(views.BaseAdminView, BaseSettings)