
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('membres/', views.membres_view, name='membres'),
    path('contact/', views.contact_view, name='contact'),
]
