from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import PostList, PostDetail

urlpatterns = patterns('',
    # Examples:
    url(r'^$', PostList.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
