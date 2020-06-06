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
    path('registration/signup', views.signup, name='signup'),
    path('registration/login', views.login, name='login'),
    path('registration/logout', views.logout, name='logout'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    path('registration/nickname/<int:user_pk>', views.nickname, name='nickname'),
    
    # home
    path('index', views.index, name='index'),
    
    # new
    path('new/category', views.new_category, name='new_category'),
    path('new/food', views.new_food, name='new_food'),
    path('new/franchise', views.new_franchise, name='new_franchies'),
    path('new/ott', views.new_ott, name='new_ott'),
    path('new/shopping', views.new_shopping, name='new_shopping'),
    path('new/others', views.new_others, name='new_others'),
    
    # edit
    path('edit/food/<int:food_pk>', views.edit_food, name='edit_food'),
    path('edit/franchise/<int:franchise_pk>', views.edit_franchise, name='edit_franchise'),
    path('edit/ott/<int:ott_pk>', views.edit_ott, name='edit_ott'),
    path('edit/shopping/<int:shopping_pk>', views.edit_shopping, name='edit_shopping'),
    path('edit/others/<int:others_pk>', views.edit_others, name='edit_others'),
    
    #delete
    path('delete/food/<int:food_pk>', views.delete_food, name='delete_food'),
    path('delete/franchise/<int:franchise_pk>', views.delete_franchise, name='delete_franchise'),
    path('delete/ott/<int:ott_pk>', views.delete_ott, name='delete_ott'),
    path('delete/shopping/<int:shopping_pk>', views.delete_shopping, name='delete_shopping'),
    path('delete/others/<int:others_pk>', views.delete_others, name='delete_others'),
    
    # detail
    path('detail/food/<int:food_pk>', views.detail_food, name='detail_food'),
    path('detail/franchise/<int:franchise_pk>', views.detail_franchise, name='detail_franchise'),
    path('detail/ott/<int:ott_pk>', views.detail_ott, name='detail_ott'),
    path('detail/shopping/<int:shopping_pk>', views.detail_shopping, name='detail_shopping'),
    path('detail/others/<int:others_pk>', views.detail_others, name='detail_others'),
    
    path('all/food', views.all_food, name='all_food'),
    path('all/franchise', views.all_franchise, name='all_franchise'),
    path('all/ott', views.all_ott, name='all_ott'),
    path('all/shopping', views.all_shopping, name='all_shopping'),
    path('all/others', views.all_others, name='all_others'),
    
    #mine
    path('myhome/mine', views.mine, name='mine'),
    path('myhome/getin', views.getin, name='getin'),
    path('myhome/editprofile', views.editprofile, name='editprofile'),
    path('myhome/delete/user', views.delete_user, name='delete_user'),
    
    #마감
    path('magam/food/<int:food_pk>', views.magam_food, name='magam_food'),
    path('magam/franchise/<int:franchise_pk>', views.magam_franchise, name='magam_franchise'),
    path('magam/ott/<int:ott_pk>', views.magam_ott, name='magam_ott'),
    path('magam/shopping/<int:shopping_pk>', views.magam_shopping, name='magam_shopping'),
    path('magam/others/<int:others_pk>', views.magam_others, name='magam_others'),
    
    path('myhome', views.myhome, name="myhome"),
]
