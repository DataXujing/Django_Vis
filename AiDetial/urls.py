from django.urls import path
from . import views

app_name = "AiDetial"

urlpatterns = [
    path('detial/<str:project>/', views.detial,name='detial'),

]