from django.db import models

# Create your models here.

#轮播图的模型
class Wheel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=50)
    class Meta:
        db_table = 'axf_wheel'

#顶部轮播图下的nav导航
class Nav(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=50)
    class Meta:
        db_table = 'axf_nav'

#顶部轮播图下的nav导航
class MustBuy(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=50)
    class Meta:
        db_table = 'axf_mustbuy'

#便利商店
class Shop(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=50)
    class Meta:
        db_table = 'axf_shop'


# mainShow 主要卖的商品 首页下面的商品
class MainShow(models.Model):
    trackid =  models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=50)
    brandname = models.CharField(max_length=50)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=50)
    productid1 = models.CharField(max_length=50)
    longname1 = models.CharField(max_length=70)
    price1 = models.CharField(max_length=50)
    marketprice1 = models.CharField(max_length=50)
    img2 = models.CharField(max_length=50)
    childcid2 = models.CharField(max_length=50)
    productid2 = models.CharField(max_length=50)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=50)
    marketprice2 = models.CharField(max_length=50)
    img3 = models.CharField(max_length=50)
    childcid3 = models.CharField(max_length=50)
    productid3 = models.CharField(max_length=50)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=50)
    marketprice3 = models.CharField(max_length=50)
    class Meta:
        db_table = 'axf_mainshow'

class FoodTypes(models.Model):
    typeid = models.CharField(max_length=50)
    typename = models.CharField(max_length=50)
    childtypenames = models.CharField(max_length=150)
    typesort = models.IntegerField()
    class Meta:
        db_table = 'axf_foodtypes'

class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=50)
    # 图片
    productimg = models.CharField(max_length=100)
    # 名字
    productname = models.CharField(max_length=50)
    # 长名字
    productlongname = models.CharField(max_length=50)
    # 是否精选
    isxf = models.BooleanField(default=False)
    # 是否买一增一
    pmdesc = models.BooleanField(default=False)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.CharField(max_length=20)
    # 原价
    marketprice = models.CharField(max_length=20)
    # 商品组id
    categoryid = models.CharField(max_length=50)
    # 商品子组id
    childcid = models.CharField(max_length=50)
    # 商品子组名名称
    childcidname = models.CharField(max_length=50)
    # 详情页id
    dealerid = models.CharField(max_length=50)
    # 库存
    storenums = models.CharField(max_length=50)
    # 销量
    productnum = models.CharField(max_length=50)
    class Meta:
        db_table = 'axf_goods'

class User(models.Model):
    userAccount = models.CharField(max_length=11)
    userPass = models.CharField(max_length=32)
    userName = models.CharField(max_length=20)
    userPhone = models.CharField(max_length=11)
    userAdderss = models.CharField(max_length=200)
    userImg = models.CharField(max_length=20)
    class Meta:
        db_table = 'axf_user'


class Cart(models.Model):
    userAccount = models.CharField(max_length=11)
    goodsId = models.CharField(max_length=11)
    goodsName =  models.CharField(max_length=50)
    goodsImg = models.CharField(max_length=150)
    goodsPrice = models.CharField(max_length=50)
    goodsNum = models.IntegerField()
    isChoose = models.BooleanField(default=False)
    class Meta:
        db_table = 'axf_cart'


