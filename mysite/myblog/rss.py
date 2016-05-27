from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from myblog.models import Post
from myblog.views import detail_view


class PostFeed(Feed):
    title = "MyBlog RSS Feed"
    link = "/rss"
    description = "An RSS feed example for MyBlog"

    def items(self):
        return Post.objects.order_by('-published_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse(detail_view, args=[item.pk])

    def item_author_name(self, item):
        return item.author

    def item_pubdate(self, item):
        return item.published_date

    def item_updateddate(self, item):
        return item.modified_date

    def item_categories(self, item):
        return [cat.name for cat in item.categories.all()]

    def ttl(self):
        #For debugging, set the TTL low so that the RSS reader
        #doesn't cache the data.
        return "1"