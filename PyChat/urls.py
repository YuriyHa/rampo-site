"""PyChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from registration import views as rv

urlpatterns = [
    path('api/v1/', include(('news.api.urls', 'post-api'))), 
    # path('api/v2/', include(('group.api.urls', 'group-api'))), 
    path('sicrit-idi-nahuy-suka/', admin.site.urls),
    path("", include("chat.urls")),
    path("news/", include("news.urls")),
    path('signup/', rv.SignUp, name="register"),
    path('deleteuser/<str:username>', rv.delete, name="delete"),
    path('user/<str:username>', rv.userdata, name="userdata"),
    path('group/', include('group.urls')),
    path("", include("django.contrib.auth.urls")),
]
