"""textutils URL Configuration

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
from django.urls import path
from  .import views


#Code for video 6
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #The first argument of path is a blank string(it specifies what to append after url)
#     path('',views.index,name='index') , #Home is pointing(endpoint) to views.index function.'' because nothing to append as it is the home page
#     path('about',views.about,name='about')   #Go to about which is in the file views with name as about
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index') ,
    path('analyze',views.analyze,name='analyze') ,
    # path('capitalizefirst',views.capfirst,name='capfirst') ,
    # path('newlineremove',views.newlineremove,name='newlineremove') ,
    # path('spaceremove',views.spaceremove,name='spaceremove') ,
    # path('charcount',views.charcount,name='charcount') ,
]
