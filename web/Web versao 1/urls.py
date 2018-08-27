from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'simplemooc.core.views.home', name='home'),#url vazia
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),#url contato
    url(r'^graficos/$', 'simplemooc.core.views.graficos', name='graficos'),#url grafico

    url(r'^g/$', 'simplemooc.core.views.g', name='g'),
    url(r'^porano/$', 'simplemooc.core.views.porano', name='porano'),
    url(r'^dashboard/$', 'simplemooc.core.views.dashboard', name='dashboard'),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
