from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .models import Profile
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth

def send_email(request):
    user = User.objects.create_user(
        username=request.POST['id'], 
        password=request.POST['password1'])
    user.is_active = False # 유저 비활성화
    user.save()
    current_site = get_current_site(request) 
    message = render_to_string(
        'registration/activation_email.html', 
            {
            'user': user,
            # 'domain': current_site.domain,
            'domain': 'https://bbc1a95c55f7.ngrok.io',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            } 
        )
    mail_title = "계정 활성화 확인 이메일"
    mail_to = request.POST["id"] + "@korea.ac.kr"
    email = EmailMessage(mail_title, message, to=[mail_to])
    email.content_subtype = 'html'
    email.send()

def nick_location(request,user_pk):
    user = User.objects.get(pk = user_pk)
    found_profile = Profile.objects.filter(nickname = request.POST['nickname'])
    if len(found_profile)>0:
        error = '해당 닉네임은 이미 존재 다른거 쓰셈'
        return render(request, 'registration/nickname.html', {'error':error})
    else:
        new_profile = Profile(
            username = user,
            nickname = request.POST['nickname'],
            location = request.POST['location'],
            hidden_loc = request.POST['real_location'],
            trust = 0,
            money = 0,
            img = 0
        )
        new_profile.save()
        return new_profile
        
    
    return 
    
def login_check(request):
    username = request.POST['id']
    password = request.POST['password']
    # 로그인
    user = auth.authenticate(request, username=username, password=password)
    # 성공
    return user

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("nickname", user.pk)
    
    else:
        return render(request, 'registration/signup.html', {'error' : '계정 활성화 오류'})
    
    return