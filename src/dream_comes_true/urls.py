"""dream_comes_true URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from organisation import views as v

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.base_page),
    url(r'^', include('allauth.account.urls')),
    url(r'^', include('customer.urls', namespace='customer')), # redirects to customer.urls
    url(r'^', include('organisation.urls', namespace='organisation')), # redirects to customer.urls
    url(r'^profile/', include('userprofile.urls', namespace='profile')), # redirects to the user profile
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework_auth')), # login as a user in the API
    url(r'^api/v1/', include('rest_api.urls', namespace='rest_framework')), # use the rest_api app for all data that is neede for the API
    #url(r'create_organisation/$', v.create_organisation, name='create_organisation'),
]

# set the STATIC_ROOT for static files
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
