from django.contrib.syndication.views import Feed
from .models import Entry

class LatestPosts(Feed):
    title = "My Posts"
    link = "/feed/"
    description = "Latest Posts by Me"

    def items(self):
        return Entry.objects.published()[:5]
