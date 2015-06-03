from django.conf.urls import include, url
from django.contrib import admin
from intro.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'phasertest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'intro.views.index', name="home"),
]
