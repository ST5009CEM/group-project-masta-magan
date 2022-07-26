"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from account import views
urlpatterns = [
    path('login/',views.user_login),
    path('login/verification',views.login_verification),

    path('',views.home_page),
    path('home/',views.home_page),
    path('calander/',views.calander_page),
    path('profile/<int:id>',views.profile_page),
    path('cheat/',views.token_page), 
    path('cheat/createcheat',views.create_cheat),  
    path('login/',views.user_login),

    path('logout/',views.log_out),



    path('history/',views.history_page),
    path('report/',views.report_page), 
    path('addreport/',views.addreport_page),  






]