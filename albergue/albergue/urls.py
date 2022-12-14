"""albergue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("rosetta", include('rosetta.urls')),
    re_path("", include('applications.users.urls')),
    re_path("", include('applications.home.urls')),
    re_path("", include('applications.reservas.urls')),
    
]
# urlpatterns+=i18n_patterns(
#     path("rosetta", include('rosetta.urls')),
#     re_path("", include('applications.users.urls')),
#     re_path("", include('applications.home.urls')),
# )
