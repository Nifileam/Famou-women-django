from django.contrib.sitemaps import Sitemap

from famouswomen.models import FamousWomen


class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return FamousWomen.published.all()

    def lastmod(self, obj):
        return obj.updated