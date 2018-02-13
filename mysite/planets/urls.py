from django.conf.urls import url
from . import views

app_name = 'planets'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'page_1/$', views.page_1)
]
