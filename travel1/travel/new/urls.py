from . import views
from django.urls import path

urlpatterns = [
    path('new1',views.new1,name='new1'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
    # path('add/',views.addition,name='addition'),

]
