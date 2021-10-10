from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    path('piano/', views.piano, name='piano'),
    path('piano2/', views.piano2, name='piano2'),
    path('piano3/', views.piano3, name='piano3'),
    path('piano_secret/', views.piano_secret, name='piano_secret'),
    path('bed_room/', views.bed_room, name='bed_room'),
    path('clock/', views.clock, name='clock'),
    path('box/', views.box, name='box'),
    path('box_left/', views.box_left, name='box_left'),
    path('box_right/', views.box_right, name='box_right'),
    path('table_recipe/', views.table_recipe, name='table_recipe'),
    path('book_recipe/', views.book_recipe, name='book_recipe'),
    path('book_recipe2/', views.book_recipe2, name='book_recipe2'),
    path('notes/', views.notes, name='notes'),
]