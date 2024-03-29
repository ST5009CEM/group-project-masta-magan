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
from user import views
urlpatterns = [
    path('',views.home_page),
    path('home/',views.home_page),
    path('calander/',views.calander_page),
    path('addprofile/',views.addprofile_page),
    path('adduser/',views.next_profilepage),
    path('adduser/<int:id>',views.next),



    path('history/',views.history_page),
    path('report/',views.report_page),  
    path('login/',views.user_login),
    path('loginverification/',views.login_verification),
    path('logout/',views.log_out),
        path('addreport/',views.addreport_page),  








]