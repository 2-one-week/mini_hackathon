from .models import food, ott, shopping,franchise, others

def create_food(request):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    _new_food = food.objects.create(
        author = request.user,
        title = request.POST['title'],
        location = request.POST['location'],
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        appLink = request.POST['appLink'],
        left = request.POST['left'],
        kakaoLink = request.POST['kakaoLink'],
        baedalTip = request.POST['baedalTip'],
        memo = request.POST['memo'],
        end = 0
        )
    return _new_food

def create_franchise(request):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    shop_name = request.POST['shop_name']
    shop_detail = request.POST['shop_detail']
    _new_franchise = franchise.objects.create(
        author = request.user,
        title = request.POST['title'],
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        shop = shop_name+shop_detail,
        item = request.POST['item'],
        event = request.POST['event'],
        kakaoLink = request.POST['kakaoLink'],
        memo = request.POST['memo'],
        end = 0
    )
    return _new_franchise

def create_shopping(request):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    _new_shopping = shopping.objects.create(
        author = request.user,
        title = request.POST['title'],
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        siteLink = request.POST['siteLink'],
        left = request.POST['left'],
        memo = request.POST['memo'],
        end = 0
    )
    return _new_shopping

def create_ott(request):
    _new_ott = ott.objects.create(
        author = request.user,
        title = request.POST['title'],
        people = request.POST['people'],
        kakaoLink = request.POST['kakoLink'],
        memo = request.POST['memo'],
        end = 0
    )
    return _new_ott

def create_others(request):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    _new_others = others.objects.create(
        author = request.user,
        title = request.POST['title'],
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        siteLink = request.POST['siteLink'],
        kakaoLink = request.POST['kakoLink'],
        memo = request.POST['memo'],
        end = 0
    )
    return _new_others