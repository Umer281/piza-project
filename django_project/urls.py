"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from practice_blog import views as practice_blog_views
from practice_user import views as practice_user_views
from Piza import views as Piza_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('blog/',include('blog.urls')),
    path('practice_blog',practice_blog_views.phome,name='practice blog'),
    path('practice_user',practice_user_views.pracregister,name='practice user'),
    path('prac_login',auth_views.LoginView.as_view(template_name='practice_user/prac_login.html'),name='prac_login'),
    path('prac_logout',auth_views.LogoutView.as_view(template_name='practice_user/prac_logout.html'),name='prac_logout'), 
    path('order/',Piza_views.order,name='order'),
    path('items/',Piza_views.items,name='items'),
    path('storeditems/',Piza_views.storeditems,name='storeditems'),
    
    
]
