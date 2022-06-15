from django.db import models
from django.utils import timezone
from django.conf import settings
from main.models import Monk

class Prayer(models.Model):
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulum = models.CharField(max_length=255)
    oratio = models.TextField()
    creatio = models.DateTimeField(default=timezone.now)
    publicatio = models.DateTimeField(blank=True, null=True)
    amens = models.ManyToManyField(to=Monk, related_name="amenned_prayers")

    def __str__(self):
        return self.titulum

    def count_amens(self):
        return self.amens.count()

    def amenners_list(self):
        amenners_list = []            
        monks_list = Monk.objects.order_by('id')
        for monk in monks_list:
            if self.amens.filter(id=monk.id).exists():
                amenners_list.append(monk.id)

        return amenners_list

class Comment(models.Model):
    prayer = models.ForeignKey(Prayer, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='Incognito')
    text = models.TextField()
    publicatio = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.prayer.titulum, self.name)
