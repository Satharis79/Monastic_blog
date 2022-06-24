from django.db import models
from django.conf import settings
from main.models import Monk

class Prayer(models.Model):
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulum = models.CharField(max_length=255)
    oratio = models.TextField()
    creatio = models.DateTimeField(auto_now_add=True)
    publicatio = models.DateTimeField(blank=True, null=True)
    amens = models.ManyToManyField(to=Monk, related_name="amenned_prayers")

    def __str__(self):
        return self.titulum

    def count_amens(self):
        return self.amens.count()

class Comment(models.Model):
    prayer = models.ForeignKey(Prayer, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='Incognito')
    text = models.TextField()
    publicatio = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.prayer.titulum, self.name)
