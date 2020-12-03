from django.db import models

# Create your models here.

# Index页面的Table
class Aiscore(models.Model):

    title = models.CharField(max_length=300)
    partner = models.CharField(max_length=100)
    describe = models.CharField(max_length=2000)
    createdate = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "项目信息表"
        ordering = ['-createdate'] 
