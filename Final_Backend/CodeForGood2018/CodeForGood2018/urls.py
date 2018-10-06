
"""CodeForGood_API URL Configuration

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
from django.conf.urls import url, include

from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'CodeForGood API'
API_DESCRIPTION = 'API Documentation'
schema_view = get_swagger_view(title = API_TITLE)

urlpatterns = [
    #url(r'^erbuddyapi/',include('apps.phonecase_t1.urls',namespace = 'phonecase_t1')),
    #url(r'^CodeForGoodapi/',include('apps.utilities.urls', namespace = 'utilities')),
    url(r'^CodeForGoodapi/',include(('apps.authentication.urls','authentication'),namespace='authentication')),
    url(r'^admin/', admin.site.urls),
    url(r'^swagger-docs/',schema_view),
]


