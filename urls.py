from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name='home'),
    path("Product/", views.Product,name='Product'),
    path("Pricing/", views.Pricing,name='Pricing'),
    path("About/", views.About,name='About'),
    path("Contect/", views.Contect,name='Contect'),
    path("Page/", views.Page,name='Page'),
    path("login/", views.login_view,name='login'),
    path("signup/", views.signup,name='signup'),
]