"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view()),
	url(r'^profile/([a-zA-Z0-9_.-]+$)', ProfilePage.as_view()),
	url(r'^profile/', ProfilePage.as_view()),
    url(r'^rec/$', RecPage.as_view()),
	url(r'^rec/([a-zA-Z0-9_.-]+$)', RecPage.as_view()),
    url(r'^login/', LoginPage.as_view()),
	url(r'^logout/', Logout.as_view()),
	url(r'^error/([a-zA-Z0-9_.-]+$)', ErrorPage.as_view()),
	url(r'^anime/([a-zA-Z0-9_.-]+$)', ViewAnime.as_view()),
	url(r'^add/anime$', AddAnime.as_view()),
	url(r'^edit/anime/([a-zA-Z0-9_.-]+$)', EditAnime.as_view()),
	url(r'^add/tags$', AddTags.as_view())
]
