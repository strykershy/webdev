
from django.conf.urls import url
from . import views


app_name = 'articles'

urlpatterns = [
    url(r'^$', views.newsitems, name = "items" ),
    url(r'^(?P<slug>[\w-]+)/$', views.details, name = "detail" )
]
