from django.contrib import admin
from django.urls import URLPattern, path
from . import views

urlpatterns = [
path('',views.index, name='index'),
path('aboouut',views.about,name="about"),
path('contect',views.contect,name="contact"),
path('foot',views.foot,name="foot"),
path('footer',views.footer,name="footer"),
path('gallery',views.gallery,name="gallery"),
path('home',views.home,name="home"),
path('login',views.login,name="login"),
path('nav',views.nav,name="views"),
path('navv',views.nav2,name="navwe"),
path('signup',views.signup,name="signup"),
path('settings',views.settings,name="settings"),
path("team",views.team,name="team"),
path('beach',views.beach,name="beach"),
path('agra',views.agra,name="agra"),
path('delhi',views.delhi,name="delhi"),
path('haridwar',views.haridwar,name="hari"),
path('hilll',views.hill,name="hill"),
path('history',views.history,name="history"),
path('honey',views.honey,name="honey"),
path('india',views.india,name="india"),
path('jaipur',views.jaipur,name="jaipur"),
path('mathura',views.mathura,name="mathura"),
path('parks',views.parks,name="parks"),
path('religioou',views.religious,name="religious"),
path('varnsai',views.varanasi,name="varanasi"),
path('vrind',views.vrind,name="vrind"),

]