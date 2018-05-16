from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse

from .models import Wheel,Nav,MustBuy,Shop,MainShow,Goods,FoodTypes,User,Cart
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import os
import random

def home(request):
    #轮播图数据
    wheelData = Wheel.objects.all()
    #导航数据
    navData = Nav.objects.all()
    #必买品 拖拽图片的数据
    mustBuyData = MustBuy.objects.all()
    # 便利商店
    shopData = Shop.objects.all()
    shopOne =  shopData[0]
    shopTwo =  shopData[1:3]
    shopThree =  shopData[3:7]
    shopFour =  shopData[7:11]
    # mainshow 首页下面的商品
    mainShowData = MainShow.objects.all()
    return render(request,'myApp/home.html',{'wheel':wheelData,'nav':navData,'mustbuy':mustBuyData,'shopOne':shopOne,'shopTwo':shopTwo,'shopThree':shopThree,'shopFour':shopFour,'mainshow':mainShowData})

#categoryid 商品类别的id
# childcid 大类别下的子类别
# 按照价格等等排序的id
def market(request,categoryid,childcid,orderById):
    typeData = FoodTypes.objects.all().order_by('typesort')
    if childcid=='0':
        # 通过类别筛选出来当前类别下的商品
        goodsData = Goods.objects.filter(categoryid = categoryid)
    else:
        goodsData = Goods.objects.filter(categoryid = categoryid,childcid=childcid)

    if orderById == 2:
        goodsData = goodsData.order_by('productnum')
    elif orderById == 3:
        goodsData = goodsData.order_by('price')
    elif orderById == 4:
        goodsData = goodsData.order_by('-price')

    childTypeName = FoodTypes.objects.get(typeid=categoryid).childtypenames
    childTypeList = childTypeName.split('#')
    # print(childTypeList)
    childInfo = []
    for i in childTypeList:
        type2 = i.split(':')
        childInfo.append({'childName':type2[0],'childcid':type2[1]})
    print(childInfo)
    return render(request,'myApp/market.html',{'type':typeData,'goods':goodsData,'childInfo':childInfo,'categoryid':categoryid,'childcid':childcid})



def car(request):
    userName = request.session.get('username')
    cartData = ''
    total = 0
    if userName:
        cartData = Cart.objects.filter(userAccount=userName)
        for c in cartData:
            if c.isChoose:
                total+=float(c.goodsPrice)*int(c.goodsNum)

    return render(request,'myApp/cart.html',{'username':userName,'cart':cartData,'total':total})

def mine(request):
    username = request.session.get('username')
    return render(request,'myApp/mine.html',{'username':username})

def reg(request):
    return render(request,'myApp/reg.html')

import hashlib
def doRegister(request):
    if request.method != 'POST':
        return render(request,'myApp/reg.html')
    #接收对应用户的信息
    userAccount = request.POST.get('userAccount')
    userPass = request.POST.get('userPass')
    userName = request.POST.get('userName')
    userPhone = request.POST.get('userPhone')
    userAdderss = request.POST.get('userAdderss')
    myFile = request.FILES.get('userImg')
    # 生成一个随机的名称
    imgName = myFile.name #上传文件的名称取出来
    #应该在 添加一个判断是否为图片中某种类型的文件 如果不是 则跳转回去
    if imgName.rfind('.') == -1:
        return render(request, 'myApp/reg.html')
    # 生成随机的图片名称
    newName = str(random.randrange(111111,999999))+imgName[imgName.rfind('.'):]
    filePath = os.path.join(settings.MDEIA_ROOT, newName)
    with open(filePath, 'wb') as f:
        if myFile.multiple_chunks():
            for file in myFile.chunks():
                f.write(file)
        else:
            f.write(myFile.read())
    # 再添加一个 异常处理的操作  如果出现代码异常跳转回注册页面
    md5 = hashlib.md5() #加密
    md5.update(userPass.encode('utf-8'))
    userPass = md5.hexdigest()
    try:
        user = User()
        user.userAccount = userAccount
        user.userPass = userPass
        user.userName = userName
        user.userPhone = userPhone
        user.userImg = newName
        user.userAdderss = userAdderss
        user.save()
        request.session['username'] = userAccount
    except:
        return render(request, 'myApp/reg.html')
    return render(request, 'myApp/mine.html')

# 退出登录
def doLogout(request):
    logout(request)
    return render(request,'myApp/mine.html')


def checkUsername(request):
    if request.is_ajax():
        userName = request.GET.get('name')
        myDict = {'state':2} #2为当前用户没有注册过
        if User.objects.filter(userAccount=userName).exists():
            myDict['state'] = 1 #代表注册过
        return JsonResponse(myDict)

def login(request):
    return render(request,'myApp/login.html')

# 登录ajax处理
def doLogin(request):
    userAccount = request.POST.get("userAccount")
    userPass = request.POST.get("userPass")
    user = User.objects.filter(userAccount=userAccount)
    print(user)
    if user.exists():
        # 比对密码，将密码进行hash算法后进行比较
        md5 = hashlib.md5()
        md5.update(userPass.encode("utf-8"))
        newpassword = md5.hexdigest()
        if newpassword == user.first().userPass:
            request.session["username"] = userAccount
            # 登录成功 跳转回个人中心
            return  JsonResponse({'state':200})#成功
        else:
            return  JsonResponse({'state':201})#密码不正确
    else:
        return JsonResponse({'state': 202})  # 用户不存在

# 购物车商品数量加减
def changeCart(request,state):
    # 0 商品添加1
    # 1 s商品减1
    productid = request.POST.get('productid')
    username = request.session.get("username")
    checked = '' #当前是否有选中
    if not username:
        # 没登录
        return JsonResponse({"data": -1, "status": "error"})
    cartObj = Cart.objects.filter(userAccount=username, goodsId=productid)#获取商品 是否在购物车中
    num = 0
    if state == '0':
    #     # 获取商品的数量
        productNum = Goods.objects.filter(productid=productid).first()
        if cartObj.exists():
            if int(cartObj[0].goodsNum)+1>=int(productNum.productnum):
                num = productNum.productnum
            else:
                num =int(cartObj[0].goodsNum)+1
                # print(cartObj[0])
            Cart.objects.filter(userAccount=username, goodsId=productid).update(goodsNum = num)
        else:
            cart = Cart()
            cart.userAccount = username
            cart.goodsName = productNum.productlongname
            cart.goodsId = productid
            cart.goodsImg = productNum.productimg
            cart.goodsPrice = productNum.price
            cart.goodsNum = 1
            cart.save()
            num = 1
    if state == '1':
    #     # 获取商品的数量
        productNum = Goods.objects.filter(productid=productid).first().productnum
        if cartObj.exists():
            if int(cartObj[0].goodsNum)-1>0:
                num = int(cartObj[0].goodsNum)-1
            else:
                num = 0
                # print(cartObj[0])
            Cart.objects.filter(userAccount=username, goodsId=productid).update(goodsNum = num)
        if num == 0:
            Cart.objects.filter(userAccount=username, goodsId=productid).delete()
    # 计算购物车中选择的商品的价格
    cartData = Cart.objects.filter(userAccount=username)
    # 2选择
    if state == '2':
        if cartObj[0].isChoose:
            cartObj.update(isChoose=False)
            checked = ''
        else:
            cartObj.update(isChoose=True)
            checked = '√'
    total = 0
    for c in cartData:
        if c.isChoose:
            total += float(c.goodsPrice) * int(c.goodsNum)
    return JsonResponse({"data": num, "status": "success",'price':round(total,2),'checked':checked})
