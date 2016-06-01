from django.conf.urls import url

from myblog.views import list_view
from myblog.views import detail_view
from myblog.views import create_view
from myblog.rss import PostFeed

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name='blog_detail'),
    url(r'^create',
        create_view,
        name='blog_create'),
    url(r'^rss',
        PostFeed())

]
