from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    url(r'^current_products/$', views.Current_Product_Method),
    url(r'^current_products/(?P<pk>[0-9]+)$', views.product_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
