from django.shortcuts import render, redirect, reverse
from .models import City, Order_from, User, Restaurant, Suggest


# Create your views here.


def index(request):
    username = request.session.get('username')
    print(username)
    return render(request, 'index.html', locals())


def register(request):
    return render(request, 'register.html')


def registers(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')

        users = User.objects.all()
        print(users)
        try:
            for i in users:
                if username == i.username:
                    error = '该用户名已被注册'
                    return render(request, 'register.html', {'error': error})
            else:
                user = User()
                user.username = username
                user.email = email
                user.password = password
                if pwd != password:
                    error = '密码不一致'
                    return render(request, 'register.html', {'error': error})
                else:
                    user.save()
        except Exception as  e:
            print(e)
        return redirect(reverse('orderapp:login'))


def login(request):
    return render(request, 'login.html')


def logins(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if username == user.username and password == user.password:
            request.session['username'] = request.POST['username']
            return redirect(reverse('orderapp:index'))
        else:
            error = '用户名与密码不一致'
            return render(request, 'login.html', {'error': error})


def loginout(request):
    request.session.clear()
    return redirect('orderapp:index')


def popular(request):
    restaurant = Restaurant.objects.all()
    username = request.session.get('username')
    print('---', restaurant)
    for i in restaurant:
        print('+++>', i.rname)
    return render(request, 'popular-Restaurents.html', locals())


def order(request):
    ord = Order_from.objects.all()
    restaurant = Restaurant.objects.all()
    username = request.session.get('username')
    city = City.objects.all()
    return render(request, 'order.html', locals())


def orders(request):
    if request.method == 'GET':

        return render(request, 'order.html')
    else:
        type1 = request.POST['type1']
        loca = request.POST['loca']
        city_name = request.POST['city_name']
        rname = request.POST['rname']

        ored = Order_from()
        re = Restaurant()
        ct = City()
        ored.order_type = type1
        re.location = loca
        re.rname = rname
        ct.city_name = city_name
        print(request.session.get('username'))
        if request.session.get('username'):
            ored.save()
            re.save()
            ct.save()
            print('成功')
            return render(request, 'index.html')
        else:
            error = '请登录'
            ord = Order_from.objects.all()
            restaurant = Restaurant.objects.all()
            username = request.session.get('username')
            city = City.objects.all()
            return render(request, 'order.html', locals())


def contact(request):
    return render(request, 'contact.html')


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    elif request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['Message']
        suggest = Suggest()
        suggest.subject = subject
        suggest.message = message
        suggest.save()
        return render(request, 'index.html')
