"""blog URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.flatpages import views
from blogpost.views import *
import django_comments.urls
import rest_framework.urls
from rest_framework import routers
from blogpost.api import BlogpostSet

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost', BlogpostSet, 'Blogpost')

urlpatterns = [
    url(r'^$', index),
    url(r'^blog/(?P<slug>[^\.]+).html', view_post, name='view_blog_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^pages/(?P<url>.*/)$', views.flatpage),
    url(r'^comments/', include(django_comments.urls)),
    url(r'^api-auth/', include(rest_framework.urls, namespace='rest_framework')),
    url(r'^api/', include(apiRouter.urls)),
] 

