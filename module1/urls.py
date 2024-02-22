from django.contrib import admin
from django.urls import path
from .views import *

'''urlpatterns = [
    path('admin/', admin.site.urls),
]
'''
urlpatterns = [
    path("hello2/",hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('favdestinations/',favdestinations,name='favdestinations'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/', print1, name='print1'),
    path('ran1/',ran,name='ran'),
    path('ran/',random123,name='random123'),
    path('g/',getdate1,name='getdate1'),
    path('getdate/',get_date,name='get_date'),
    path('t/',timezfunc,name='timezfunc'),
    path('functioncall/',functioncall,name='functioncall'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('w/',weatherlogic,name='weatherlogic'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('signup1/',signup1,name='signup1'),
    path('login1/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('feedback/',feedback,name='feedback'),
    path('contactmail/',contactmail,name='contactmail'),
]