from django.conf.urls import include, url
from django.contrib import admin

from .views import(
    index,
)

urlpatterns = [
    url(r'^$', index, name="home"),

]