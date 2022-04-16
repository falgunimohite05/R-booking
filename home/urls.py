from django.contrib import admin
from django.urls import path,include
import features
from .views import Index,Register,Login,home,logout,Contact
from features import views
app_name='home'
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('index',Index.as_view(),name='index'),
    path('home', home, name='home'),

    #path('index',Index.as_view(),name='index'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('contact', Contact.as_view(), name='contact'),
    path('search/',features.views.search),
    path('search/trains',features.views.getTrains),
    path('schedule/',features.views.schedule),
    path('schedule/trains',features.views.getTinfo,name='tr'),
    #path('home', Home.as_view(), name='home'),
    path('search/search/trains/cva/', features.views.cva),
    path('search/book1/', features.views.book1),
    path('search/book1/book/', features.views.book),
    path('cancel/', features.views.cancel),
    path('cancel/cancel/cn/', features.views.cn),
    path('pnr/', features.views.pnr, name="pnr"),
    ]