"""
URL configuration for crm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CRM_APP import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # admin 
    path('admin/', admin.site.urls),
    
    # dasjboard

    path('', views.dashboard, name='dashboard'),
    
    
    # User authentication
    path("signup/",views.SignupView.as_view(),name="signup"),
    path("login/",views.SigninView.as_view(),name="signin"),
    path("logout/",views.Logout_View,name="logout"),

    # Customer management
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_create, name='customer_create'),
    path('customers/edit/<int:id>/', views.customer_update, name='customer_update'),
    path('customers/delete/<int:id>/', views.customer_delete, name='customer_delete'),
]