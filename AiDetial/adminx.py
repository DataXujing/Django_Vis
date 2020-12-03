

import xadmin
from .models import Aidetial, Aidata, Aisort, Aidemo
from xadmin import views

# class BlogAdmin(object):
#   # 设置后台展示字段
#     list_display = ['name', 'desc', 'detail']
#     # 设置后台搜索字段 # 注意搜索字段不能有时间类型，否则会报错
#     search_fields = ['name']
#     # 设置后台过滤筛选字段，时间字段可以用过滤字段
#     list_filter = ['name']


class AidetialAdmin(object):
    list_display = ['title', 'createdate', 'detail']
    search_fields = ['title']
    list_filter = ['title']
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Aidetial, AidetialAdmin)


class AidataAdmin(object):
    list_display = ['title', 'createdate', 'content_text']
    search_fields = ['title']
    list_filter = ['title']
    style_fields = {"content_text": "ueditor"}


xadmin.site.register(Aidata, AidataAdmin)


class AisortAdmin(object):
    list_display = ['title',  "model_name", 'score', 'test_type','createdate']
    search_fields = ['title']
    list_filter = ['title']
    # style_fields = {"detail": "ueditor"}


xadmin.site.register(Aisort, AisortAdmin)


class AidemoAdmin(object):
    list_display = ['title', 'createdate','detail']
    search_fields = ['title']
    list_filter = ['title']
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Aidemo, AidemoAdmin)



class BaseSettings(object):
    enable_themes = True   # 使用主题功能
    use_bootswatch = True
    
# xadmin.site.register(views.BaseAdminView, BaseSettings)