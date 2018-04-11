from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool

from django.db import models


class ArticleListItemPlugin(CMSPlugin):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='articles/thumbs', blank=True)
    call_to_action_text = models.CharField(max_length=50, default='Read more', blank=True)
    call_to_action_url = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title
