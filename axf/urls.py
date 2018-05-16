from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.home, name="home"),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name="market"),
    url(r'^cart/', views.car, name="cart"),
    url(r'^mine/', views.mine, name="mine"),
    url(r'^reg/', views.reg, name="reg"),
    url(r'^doreg/', views.doRegister, name="doRegister"),
    url(r'^logout/', views.doLogout, name="dologout"),
    url(r'^login/', views.login, name="login"),
    url(r'^dologin/', views.doLogin, name="dologin"),
    url(r'^checkUsername/', views.checkUsername, name="checkUsername"),
    url(r'^changeCart/(\d)+/', views.changeCart, name="changeCart"),
]