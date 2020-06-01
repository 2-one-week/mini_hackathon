from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

def start(request):
    return render(request, 'registration/start.html')

def signup(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['id'])
        
        if len(found_user)>0:
            error = '해당 아이디는 이미 존재 다른거 쓰셈'
            return render(request, 'registration/signup.html', {'error':error})
        
        elif request.POST['password1'] ==request.POST['password2']:
            # 유저 만들기
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
                    'domain': current_site.domain,
                    # 'domain': 'https://2791c9da0029.ngrok.io',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    }
                )
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST["id"] + "@korea.ac.kr"
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return HttpResponse(
                '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                'justify-content: center; align-items: center;">'
                '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
                '</div>'
            )

    # 포스트 방식 아니면 페이지 띄우기
    return render(request, 'registration/signup.html')


def nickname(request, user_pk):
    if request.method == 'POST':
        print(request.POST['location'])
        user = User.objects.get(pk = user_pk)
        new_profile = Profile(
            user = user,
            nickname = request.POST['nickname'],
            location = request.POST['location'],
            hidden_loc = request.POST['real_location']
        )
        new_profile.save()
        return redirect('index')
    return render(request, 'registration/nickname.html')

def login(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 정보 가져와서 
        username = request.POST['id']
        password = request.POST['password']
        # 로그인
        user = auth.authenticate(
            request, 
            username=username, 
            password=password)
        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        # 실패
        else:
            return render(request, 
                          'registration/login.html', 
                          {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
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

# --------------------------------------------------------------로그인 기능---------------------

def index(request):
    return render(request, 'index.html')
