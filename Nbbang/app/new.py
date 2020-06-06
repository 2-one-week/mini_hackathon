from .models import food, ott, shopping,franchise, others

def create_food(request):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    shop_loc = request.POST['appLink'].find("'",2)
    loc = request.POST['appLink'].find('https')
    _shop = request.POST['appLink'][1:shop_loc]
    url = (request.POST['appLink'][loc:])
    save_money = int(request.POST['baedalTip'])/2
    _new_food = food.objects.create(
        author = request.user,
        title = request.POST['title'],
        location = request.user.profile.location,
        author_location = request.user.profile.hidden_loc,
        shop = _shop,
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        appLink = url,
        left = request.POST['left'],
        kakaoLink = request.POST['kakaoLink'],
        baedalTip = request.POST['baedalTip'],
        memo = request.POST['memo'],
        end = 0,
        savemoney = save_money
        )
    return _new_food

def create_franchise(request):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    shop_name = request.POST['shop_name'] + request.POST['shop_detail']
    _new_franchise = franchise.objects.create(
        author = request.user,
        location = request.user.profile.location,
        title = request.POST['title'],
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        shop = shop_name,
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
        service = request.POST['OTT-service'],
        people = request.POST['people'],
        kakaoLink = request.POST['kakaoLink'],
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
        kakaoLink = request.POST['kakaoLink'],
        memo = request.POST['memo'],
        end = 0
    )
    return _new_others