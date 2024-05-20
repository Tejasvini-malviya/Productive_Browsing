"""
URL configuration for browsering project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name="dashboard"),
    path('add_restricted_site/', add_restricted_site, name="dashboard"),
    path('delete_restricted_site/<int:site_id>', delete_restricted_site, name="delete_restricted_site"),
    path('add_time_limit/', add_time_limit, name="add_time_limit"),
    path('delete_time_limit/<int:limit_id>', add_time_limit, name="add_time_limit"),
    path('all_urls_data/', AllUrlsDataView.as_view(), name="all_urls_data"),
]
