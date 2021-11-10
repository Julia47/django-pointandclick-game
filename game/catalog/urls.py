from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from catalog.models import GameUser, Note, Question
from django.db.models import Count
from django.urls import include, re_path

# import django_filters
# app_name = "game"
urlpatterns = [
    path('piano2/', views.piano2, name='piano2'),
    path('notes/', views.notes, name='notes'),
    path('register/', views.register_request, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name="registration/logged_out.html"),
         name='logout'),
    path('note_template/', views.note_template, name='note_template'),
    path('load_view/<id_url>/', views.load_view, name='load_view'),
    path('load_note/', views.load_note, name='load_note'),
    re_path('load_question?(?P<slug>[\w-]+)/$', views.load_question, name='load_question'),
    path('test_data/', views.test_data, name='test_load'),
]
