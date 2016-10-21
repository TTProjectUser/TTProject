from django.shortcuts import render
from django.utils import timezone
from .models import Activity
import datetime

def calendar_view(request):

    def get_current_week(date):
        first_day = date - datetime.timedelta(days=date.weekday())
        last_day = first_day + datetime.timedelta(days=4)
        return first_day.strftime("%d %b"), last_day.strftime("%d %b %Y")


    def get_hours(last_hour):
        return [str(i) + ':00' for i in range(8, last_hour+1)]


    first_day, last_day = get_current_week(timezone.now())
    day_hours = get_hours(20)
    activites = Activity.objects.filter(user=request.user)
    weekdays = set(sorted([act.get_day_abbrv() for act in activites]))
    return render(request, 'timetracker/base.html', {'activites': activites, 'weekdays': weekdays,
                                                     'first_day': first_day, 'last_day': last_day,
                                                     'hours': day_hours})
