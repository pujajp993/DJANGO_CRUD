from django.urls import path,include
from AA_app import views


urlpatterns = [
    
    path('index',views.userindex,name='userindex'),
    path('login',views.login,name='login'),
    path('viewdata',views.viewdata,name='viewdata,'),
    path('viewall',views.viewall,name='viewall,'),
    path('nupdate/<int:uid>',views.nupdate,name='nupdate'),
    path('ndelete/<int:uid>',views.ndelete,name='ndelete'),
]

