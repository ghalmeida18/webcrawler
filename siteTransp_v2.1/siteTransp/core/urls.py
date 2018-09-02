from django.conf.urls import url
from siteTransp.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contact, name='contact'),
]
