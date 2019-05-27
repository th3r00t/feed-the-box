from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.index, name='search'),
    path('download', views.download, name='download')
]
