"""Nbbang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from app import views

urlpatterns = [
    # admin page
    path('admin/', admin.site.urls),
    
    # 로그인 및 닉네임, 인증 토큰
    path('', views.start, name='start'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.login, name='logout'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    path('nickname/<int:user_pk>', views.nickname, name='nickname'),
    
    # home
    path('index', views.index, name='index'),
    
    # new
    path('new/category', views.new_category, name='new_category'),
    path('new/food', views.new_food, name='new_food'),
    path('new/franchise', views.new_franchies, name='new_franchies'),
    path('new/ott', views.new_ott, name='new_ott'),
    path('new/shopping', views.new_shopping, name='new_shopping'),
    path('new/others', views.new_others, name='new_others'),
    
    # edit & delete
    
]
