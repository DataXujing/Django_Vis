from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


class Aidetial(models.Model):
    title = models.CharField(max_length=200, verbose_name='项目名称')
    createdate = models.DateField(auto_now_add=True,verbose_name='创建日期')
    detail = UEditorField(verbose_name='项目介绍',width=800, height=500, toolbars="full", 
        imagePath="static/upload/ueditor/%(datetime)s.%(extname)s", 
        filePath="static/upload/ueditor/%(datetime)s.%(extname)s", 
        upload_settings={"imageMaxSize":1204000},
        default='')

    class Meta:
        verbose_name_plural = '项目细节'
        get_latest_by = 'createdate'



class Aidata(models.Model):
    title = models.CharField(max_length=200, verbose_name='项目名称')
    createdate = models.DateField(auto_now_add=True,verbose_name='创建日期')
    content_text = UEditorField(verbose_name='数据和评价指标',width=800, height=500, toolbars="full", 
        imagePath="static/upload/ueditor/%(datetime)s.%(extname)s", 
        filePath="static/upload/ueditor/%(datetime)s.%(extname)s", 
        upload_settings={"imageMaxSize":1204000},
        default='')



    class Meta:
        verbose_name_plural = '数据和评价指标'

class Aisort(models.Model):
    title = models.CharField(max_length=200, verbose_name='项目名称')
    model_name = models.CharField(max_length=200, verbose_name='使用的模型')
    score = models.FloatField(verbose_name='得分')
    test_type = models.CharField(max_length=20, verbose_name='榜单类型')
    createdate = models.DateField(auto_now_add=True,verbose_name='创建日期')

    class Meta:
        verbose_name_plural = '项目排名'


class Aidemo(models.Model):
    title = models.CharField(max_length=200, verbose_name='项目名称')
    createdate = models.DateField(auto_now_add=True,verbose_name='创建日期')
    detail = UEditorField(verbose_name='效果展示',width=800, height=500, toolbars="full", 
        imagePath="static/upload/ueditor/%(datetime)s.%(extname)s", 
        filePath="static/upload/ueditor/%(datetime)s.%(extname)s", 
        upload_settings={"imageMaxSize":1204000},
        default='')

    class Meta:
        verbose_name_plural = '效果展示'
        get_latest_by = 'createdate'






