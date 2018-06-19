from django.urls import path
import FreeMusic.settings as settings

from main import views

urlpatterns = [
    path('', views.home),
    path('images/<item>/', views.redirectToImages),
    path('js/<item>/', views.redirectToJs),
    path('js/<folder>/<item>/', views.redirectToJsFolder),
    path('js/<folder>/<folder2>/<item>/', views.redirectToJsFolder2),
    path('css/<item>/', views.redirectToCss),
    path('fonts/<item>/', views.redirectToFonts),
]
