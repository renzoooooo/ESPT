from django.contrib import admin
from django.urls import path
from esportscentresys.views import *
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('model1_custominfo.html', views.custominfo,name="CustomInfo")

]
