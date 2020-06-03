from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# sign up
from .models import Profile, food, ott, shopping,franchise, others
from .start import send_email, nick_location, login_check,activate_account
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token

# new 

# -----------------------로그인 기능---------------------
# 첫번쨰 시작시 페이지
def start(request):
    return render(request, 'registration/start.html')

# 고대 인증 메일 보내내는 과정
def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['id'])
        
        if len(found_user)>0:
            error = '해당 아이디는 이미 존재 다른거 쓰셈'
            return render(request, 
                          'registration/signup.html', 
                          {'error':error})
        
        elif request.POST['password1'] ==request.POST['password2']:
            send_email(request)
            return render(request,'registration/wait.html')
        
    return render(request, 'registration/signup.html')

# 인증 성공 시 닉네임 + 위치 받아오기
def nickname(request, user_pk):
    if request.method == 'POST':
        new_profile = nick_location(request,user_pk)
        return redirect('index', new_profile)
    return render(request, 'registration/nickname.html')

def login(request):
    if request.method == 'POST':
        user = login_check(request)
        if user is not None:
            profile = Profile.objects.filter(username = user)
            auth.login(request, user)
            return redirect('index', profile[0])
        else:
            return render(request, 'registration/login.html', {'error': '아이디 혹은 비밀번호 틀림'})
    else:
        return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    return activate_account(request, uidb64, token)

# -----------------------로그인 기능---------------------

# 홈화면
def index(request, profile):
    foods = food.objects.all()
    return render(request, 'index.html', { 'profile':profile, 'foods' : foods} )


# -----------------------new--------------------------
def new_category(request):
    return render(request, 'new/category.html')

def new_food(request):
    if request.method == "POST":
        
        return redirect('index')
    return render(request, 'new/new_food.html')

def new_franchies(request):
    return render(request, 'new/new_franchise.html')

def new_ott(request):
    return render(request, 'new/new_ott.html')

def new_shopping(request):
    return render(request, 'new/new_shopping.html')

def new_others(request):
    return render(request, 'new/new_others.html')

# -----------------------edit------------------------

# -----------------------delete------------------------