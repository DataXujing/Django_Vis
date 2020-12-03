from django.contrib import admin

# Register your models here.

from .models import Aidetial, Aidata, Aisort, Aidemo

admin.site.register(Aidetial)
admin.site.register(Aidata)
admin.site.register(Aisort)
admin.site.register(Aidemo)
