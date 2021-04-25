from django.contrib import admin

from . import views
from django.urls import include, path


urlpatterns = [
    path('signup/',views.register,name='register'),
    path('base/',views.home,name='home'),
    path("booklist/book/<int:id>", views.index, name="index"),
    path('booklist/',views.list,name='list'),
    path('home/',views.home,name='home'),
    path('searchbook/',views.searchbook,name='searchbook'),
]