from django.shortcuts import render
from django.utils import timezone
from .models import Activity

def calendar_view(request):
    activites = Activity.objects.filter(user=request.user)
    return render(request, 'timetracker/base.html', {'activites': activites})
