from .models import food, ott, shopping,franchise, others

def update_food(request, food_pk):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    edit_food = food.objects.filter(pk = food_pk)
    edit_food.update(
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
    return edit_food

def update_franchise(request, franchise_pk):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    shop_name = request.POST['shop_name']
    shop_detail = request.POST['shop_detail']
    edit_franchise = franchise.objects.filter(pk = franchise_pk)
    edit_franchise.update(
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
    return edit_franchise

def update_shopping(request, shopping_pk):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    edit_shopping = shopping.objects.filter(pk = shopping_pk)
    edit_shopping.update(
        author = request.user,
        title = request.POST['title'],
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        siteLink = request.POST['siteLink'],
        left = request.POST['left'],
        memo = request.POST['memo'],
        end = 0
    )
    return edit_shopping

def update_ott(request, ott_pk):
    edit_ott = ott.objects.filter(pk = ott_pk)
    edit_ott.update(
        author = request.user,
        title = request.POST['title'],
        service = request.POST['OTT-service'],
        people = request.POST['people'],
        kakaoLink = request.POST['kakaoLink'],
        memo = request.POST['memo'],
        end = 0
    )
    return _new_ott

def update_others(request, others_pk):
    month = str(request.POST['month'])
    day = str(request.POST['day'])
    edit_others = ott.objects.filter(pk = others_pk)
    edit_others.update(
        author = request.user,
        title = request.POST['title'],
        deadline1 = month +'/'+day,
        deadline2 = request.POST['time'],
        siteLink = request.POST['siteLink'],
        kakaoLink = request.POST['kakoLink'],
        memo = request.POST['memo'],
        end = 0
    )
    return edit_others