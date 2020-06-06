# 기본
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# sign up
from .models import Profile, food, ott, shopping,franchise, others
from .start import send_email, nick_location, login_check,activate_account

# new 
from .new import create_food, create_franchise, create_others, create_ott, create_shopping

#update
from .edit import update_food, update_franchise, update_others, update_ott, update_shopping

from datetime import datetime

# -----------------------signup & login---------------------
# 첫번쨰 시작시 페이지
def start(request):
    if len(request.user.username)>0:
        return redirect('index')
    return render(request, 'registration/start.html')

# 고대 인증 메일 보내내는 과정
def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['id'])
        
        if len(found_user)>0:
            error = '해당 아이디는 이미 존재 다른거 쓰셈'
            return render(request, 'registration/signup.html', {'error':error})
        
        elif request.POST['password1'] ==request.POST['password2']:
            send_email(request)
            return render(request,'registration/wait.html')
        
    return render(request, 'registration/signup.html')

def nickname(request, user_pk):
    if request.method == 'POST':
        # 인증 성공 시 닉네임 + 위치 받아오기
        nick_location(request,user_pk)
        return redirect('index')
    return render(request, 'registration/nickname.html')

def login(request):
    if request.method == 'POST':
        user = login_check(request)
        if user is not None:
            auth.login(request, user)
            return redirect(request.GET.get('next', '/index'))
        else:
            return render(request, 'registration/login.html', {'error': '아이디 혹은 비밀번호 틀림'})
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    return activate_account(request, uidb64, token)

# ---------------------home---------------------------
@login_required(login_url= '/registration/login')
def index(request):
    foods = food.objects.all()
    return render(request, 'index.html', {'foods' : foods} )


# -----------------------new--------------------------
@login_required(login_url= '/registration/login')
def new_category(request):
    
    return render(request, 'new/category.html')

@login_required(login_url= '/registration/login')
def new_food(request):
    if request.method == "POST":
        _new_food = create_food(request)
        return redirect('detail_food', _new_food.pk)
        # return redirect('detail',0 , _new_food.pk)
    return render(request, 'new/new_food.html')

@login_required(login_url= '/registration/login')
def new_franchise(request):
    if request.method == "POST":
        _new_franchise = create_franchise(request)
        return redirect('detail_franchise', _new_franchise.pk)
    return render(request, 'new/new_franchise.html')

@login_required(login_url= '/registration/login')
def new_ott(request):
    if request.method == "POST":
        _new_ott = create_ott(request)
        return redirect('detail_ott', _new_ott.pk)
    return render(request, 'new/new_ott.html')

@login_required(login_url= '/registration/login')
def new_shopping(request):
    if request.method == "POST":
        _new_shopping = create_shopping(request)
        return redirect('detail_shopping', _new_shopping.pk)
    return render(request, 'new/new_shopping.html')

@login_required(login_url= '/registration/login')
def new_others(request):
    if request.method == "POST":
        _new_others = create_others(request)
        return redirect('detail_others', _new_others.pk)
    return render(request, 'new/new_others.html')

# -----------------------edit------------------------
@login_required(login_url= '/registration/login')
def edit_food(request, food_pk):
    current_food = food.objects.get(pk = food_pk)
    if request.method == 'POST':
        update_food(request, food_pk)
        return redirect('detail_food', food_pk)
    return render(request, 'edit/edit_food.html', {'food' : current_food })

@login_required(login_url= '/registration/login')
def edit_franchise(request, franchise_pk):
    current_franchise = franchise.objects.get(pk = franchise_pk)
    if request.method == 'POST':
        update_franchise(request, franchise_pk)
        return redirect('detail_franchise', franchise_pk)
    return render(request, 'edit/edit_franchise.html', {'franchise' : current_franchise })

@login_required(login_url= '/registration/login')
def edit_ott(request, ott_pk):
    current_ott = ott.objects.get(pk = ott_pk)
    if request.method == 'POST':
        update_ott(request, ott_pk)
        return redirect('detail_ott', ott_pk)
    return render(request, 'edit/edit_ott.html', {'ott' : current_ott })

@login_required(login_url= '/registration/login')
def edit_shopping(request, shopping_pk):
    current_shopping = shopping.objects.get(pk = shopping_pk)
    if request.method == 'POST':
        update_shopping(request, shopping_pk)
        return redirect('detail_shopping', shopping_pk)
    return render(request, 'edit/edit_shopping.html', {'shopping' : current_shopping })

@login_required(login_url= '/registration/login')
def edit_others(request, others_pk):
    current_others = others.objects.get(pk = others_pk)
    if request.method == 'POST':
        update_others(request, others_pk)
        return redirect('detail_others', others_pk)
    return render(request, 'edit/edit_franchise.html', {'others' : current_others })

# -----------------------delete----------------------
@login_required(login_url= '/registration/login')
def delete_food(request, food_pk):
    del_food = food.objects.get(pk = food_pk)
    del_food.delete()
    return redirect('index')

@login_required(login_url= '/registration/login')
def delete_franchise(request, franchise_pk):
    del_franchise = franchise.objects.get(pk = franchise_pk)
    del_franchise.delete()
    return redirect('index')

@login_required(login_url= '/registration/login')
def delete_ott(request, ott_pk):
    del_ott = ott.objects.get(pk = ott_pk)
    del_ott.delete()
    return redirect('index')

@login_required(login_url= '/registration/login')
def delete_shopping(request, shopping_pk):
    del_shopping = shopping.objects.get(pk = shopping_pk)
    del_shopping.delete()
    return redirect('index')

@login_required(login_url= '/registration/login')
def delete_others(request, others_pk):
    del_others = others.objects.get(pk = others_pk)
    del_others.delete()
    return redirect('index')

# -----------------------detail----------------------
@login_required(login_url= '/registration/login')
def detail_food(request, food_pk):
    current_food = food.objects.get(pk = food_pk)
    print(current_food.appLink)
    print(current_food.appLink.find('https'))
    shop_loc = current_food.appLink.find("'",2)
    loc = current_food.appLink.find('https')
    shop = current_food.appLink[1:shop_loc]
    url = (current_food.appLink[loc:])
    save_money = int(current_food.baedalTip)/2
    return render(request, 'detail/detail_food.html', {'food' : current_food, 'save_money':int(save_money), 'shop': shop, 'url': url})

@login_required(login_url= '/registration/login')
def detail_franchise(request, franchise_pk):
    current_franchise = franchise.objects.get(pk = franchise_pk)
    return render(request, 'detail/detail_franchise.html',{'franchise':current_franchise})

@login_required(login_url= '/registration/login')
def detail_ott(request, ott_pk):
    current_ott = ott.objects.get(pk = ott_pk)
    return render(request, 'detail/detail_ott.html',{'ott':current_ott})

@login_required(login_url= '/registration/login')
def detail_shopping(request, shopping_pk):
    shopping_pk = shopping.objects.get(pk = shopping_pk)
    return render(request, 'detail/detail_shopping.html',{'shopping':shopping_pk})

@login_required(login_url= '/registration/login')
def detail_others(request, others_pk):
    current_others = others.objects.get(pk =others_pk )
    return render(request, 'detail/detail_others.html', {'others':current_others})

#------------------------all_items---------------------
@login_required(login_url= '/registration/login')
def all_food(request):
    all_food = food.objects.all()
    return render(request, 'all/all_food.html', {'foods' : all_food})

@login_required(login_url= '/registration/login')
def all_franchise(request):
    all_franchise = franchise.objects.all()
    return render(request, 'all/all_franchise.html',{'franchises':all_franchise})

@login_required(login_url= '/registration/login')
def all_ott(request):
    all_ott = ott.objects.all()
    return render(request, 'all/all_ott.html',{'otts':all_ott})

@login_required(login_url= '/registration/login')
def all_shopping(request):
    all_shopping = shopping.objects.all()
    return render(request, 'all/all_shopping.html',{'shoppings':all_shopping})

@login_required(login_url= '/registration/login')
def all_others(request):
    all_others = others.objects.all()
    return render(request, 'all/all_others.html', {'others':all_others})


# -----------------------my_profile----------------------
@login_required(login_url= '/registration/login')
def myhome(request):
    return render(request, 'myhome/myhome.html')

def mine(request):
    return render(request, 'myhome/myhome-mine.html')

def getin(request):
    return render(request, 'myhome/myhome-getin.html')

def editprofile(request):
    return render(request, 'myhome/myhome-editprofile.html')

def delete_user(request):
    request.user.delete()
    return redirect('signup')

#--------------------------마감 치기------------------
@login_required(login_url= '/registration/login')
def magam_food(request, food_pk):
    magam_food = food.objects.filter(pk = food_pk)
    magam_food.update(
        end = 1
    )
    return redirect('index')

@login_required(login_url= '/registration/login')
def magam_franchise(request, franchise_pk):
    magam_franchise = franchise.objects.filter(pk = franchise_pk)
    magam_franchise.update(
            end = 1
    )
    return redirect('index')

@login_required(login_url= '/registration/login')
def magam_ott(request, ott_pk):
    magam_ott = ott.objects.filter(pk = ott_pk)
    magam_ott.update(
        end = 1
    )
    return redirect('index')

@login_required(login_url= '/registration/login')
def magam_shopping(request, shopping_pk):
    magam_shopping = shopping.objects.filter(pk = shopping_pk)
    magam_shopping.update(
        end = 1
    )
    return redirect('index')


@login_required(login_url= '/registration/login')
def magam_others(request, others_pk):
    magam_others = others.objects.filter(pk = others_pk)
    magam_others.update(
        end = 1
    )
    return redirect('index')