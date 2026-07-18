from django.urls import path
from webapp.views import *

app_name =  'webapp'
urlpatterns = [
    path("",main_view,name="index"),
]