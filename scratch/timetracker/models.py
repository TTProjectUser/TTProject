from django.db import models
from django.utils import timezone


class Activity(models.Model):
    user = models.ForeignKey('auth.User')
    type = models.CharField(max_length=100)
    started = models.DateTimeField()
    ended = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now())
    last_modification = models.DateTimeField(
                        blank=True, null=True)
    all_day = models.BooleanField(default=False)
    comment = models.CharField(max_length=300)


    def get_time_difference(self):
        return self.started - self.ended


    def get_day_abbrv(self):
        return self.started.strftime('%a')


    def __str__(self):
        return self.type
