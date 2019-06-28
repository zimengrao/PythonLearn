"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from cmdb import views as cmdb_views
# from django.urls import  reverse


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',cmdb_views.home, name='home'),
    # # path('add/', cmdb_views.add, name='add'),
    # path('add/<int:a>/<int:b>', cmdb_views.add1, name='add1'),
    # path(r'^add/(\d+)/(\d+)/$', cmdb_views.old_add1),
    # path(r'^new_add/(\d+)/(\d+)/$', cmdb_views.add1, name='add1'),
    path('admin/',admin.site.urls),

]

