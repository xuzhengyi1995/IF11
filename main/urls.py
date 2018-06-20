from django.urls import path
import FreeMusic.settings as settings

from main import views

urlpatterns = [
    path('index', views.home),
    path('', views.signIn),
    path('signup', views.signUp),
    path('tiandi', views.tianDi),
    path('images/<item>/', views.redirectToImages),
    path('js/<item>/', views.redirectToJs),
    path('js/<folder>/<item>/', views.redirectToJsFolder),
    path('js/<folder>/<folder2>/<item>/', views.redirectToJsFolder2),
    path('css/<item>/', views.redirectToCss),
    path('fonts/<item>/', views.redirectToFonts),
    path('fonts/<folder>/<item>/', views.redirectToFonts2),
    path('profile', views.returnProfile),
]
