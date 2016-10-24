from django.db import models
from django.utils import timezone
import datetime


class Activity(models.Model):
    user = models.ForeignKey('auth.User')
    type = models.CharField(max_length=100)
    started = models.DateTimeField()
    ended = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_modification = models.DateTimeField(
                        blank=True, null=True)
    all_day = models.BooleanField(default=False)
    comment = models.CharField(default='', blank=True, max_length=300)

    @property
    def get_time_difference_in_px(self):
        difference = self.ended - self.started
        return ((difference / datetime.timedelta(minutes=1)) * 2) + 6

    @property
    def get_starting_position(self):
        return (((self.started - self.started.replace(hour=6, minute=0, second=0, microsecond=0)) /
                  datetime.timedelta(minutes=1)) * 2) + 6

    @property
    def get_day_abbrv(self):
        return self.started.strftime('%a')

    def __str__(self):
        return self.type