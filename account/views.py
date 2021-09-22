import django
from django.shortcuts import render, redirect,reverse
from django.utils.timezone import now
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from account import models
# Create your views here.

#注册
class Register(View):
    def get(self,request):
        # 判断当前是否登陆，如果已登录跳转至首页
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return render(request,'account/register.html')


    def post(self,request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        check_password = request.POST.get('check_password', '')

        #判断密码与确认密码是否一致
        if password != check_password:
            return HttpResponse('两次密码输入不一致')

        #判断当前注册账号是否已经注册
        exists = User.objects.filter(username=username).exists()
        if exists:
            return HttpResponse('该用户名已注册请重新注册')
        User.objects.create_user(username=username,password=password)
        return redirect(reverse('login'))



#登陆
class Login(View):
    def get(self, request):
        return render(request,'account/login.html')

    def post(self, request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        #判断当前用户是否存在
        exists = User.objects.filter(username=username).exists()
        if not exists:
            return HttpResponse('该账号不存在请注册')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('密码错误')



#首页
class Index(View):
    def get(self, request):
        states = models.User.objects.all()
        return render(request,'account/index.html',{'result':states})

    def post(self, request):
        pass

#退出
class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))

    def post(self, request):
        pass


class date(View):
    def get(self, request):
        pass


    def post(self, request):
        uesrname = request.POST.get('uesrname','')
        goodsname = request.POST.get('goodsname','')
        goodsnum = request.POST.get('goodsnum','')
        goodsmy = request.POST.get('goodsmy','')
        createtime = request.POST.get('createtime','')

        if not all([uesrname,goodsname,goodsnum,goodsmy,createtime]):
            return HttpResponse('请填写完整信息')

        User.objects.create_user(
            uesrname = uesrname,
            goodsname = goodsname,
            goodsnum = goodsnum,
            goodsmy = goodsmy,
            createtime = createtime
        )
        return redirect(reverse('index'))

class delate(View):
    def get(self, request):
        states = models.User.objects.all()
        return render(request, 'account/index.html', {'result': states})

    def post(self, request):
        models.User.objects.filter(id=id).delete()
        states = models.User.objects.all()
        return render(request, 'account/index.html', {'result': states})

#新增
class Create(View):
    def get(self, request):
        return render(request,'account/create.html')

    def post(self, request):
        uesrname = request.POST.get('uesrname', '')
        goodsname = request.POST.get('goodsname', '')
        goodsnum = request.POST.get('goodsnum', '')
        goodsmy = request.POST.get('goodsmy', '')
        createtime = django.utils.timezone.now()
        if not all([uesrname, goodsname, goodsnum, goodsmy]):
            return HttpResponse('请填写完整信息')

        models.User.objects.create(
            uesrname=uesrname,
            goodsname=goodsname,
            goodsnum=goodsnum,
            goodsmy=goodsmy,
            createtime=createtime
        )
        return redirect(reverse('index'))
#查询
class find(View):
    def get(self, request):
        pass


    def post(self, request):
        text = request.POST.get('search', '')
        if text == '':
            states = models.User.objects.all()
        else:
            states = models.User.objects.filter(goodsname=text)
        return render(request, 'account/index.html', {'result': states})

#修改内容
class change(View):
    def get(self, request):
        pass

    def post(self, request):
        text = int(request.POST.get('search', ''))
        states = models.User.objects.filter(id=text)
        return render(request, 'account/change.html', {'result': states})

class changebtn(View):
    def post(self, request):
        id = request.POST.get('id', '')
        uesrname = request.POST.get('uesrname', '')
        goodsname = request.POST.get('goodsname', '')
        goodsnum = request.POST.get('goodsnum', '')
        goodsmy = request.POST.get('goodsmy', '')
        createtime = django.utils.timezone.now()
        if not all([uesrname, goodsname, goodsnum, goodsmy]):
            return HttpResponse('请填写完整信息')

        models.User.objects.filter(id=id).update(
            uesrname=uesrname,
            goodsname=goodsname,
            goodsnum=goodsnum,
            goodsmy=goodsmy,
            createtime=createtime
        )
        return redirect(reverse('index'))