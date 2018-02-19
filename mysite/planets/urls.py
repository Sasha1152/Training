from django.conf.urls import url
from . import views

app_name = 'planets'

urlpatterns = [
    url(r'^$', views.planets_list, name='planets_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.planet_data, name='planet_data'),
    url(r'page_1/$', views.page_1),
    url(r'page_2/$', views.page_2),

]
