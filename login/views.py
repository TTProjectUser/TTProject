from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Activity


@csrf_exempt
def index(request):

    arr_act = Activity.objects.all()
    arr_act.order_by('start')
    new_arr = list()

    for i in range(0, arr_act.count()):
        if i == 0:
            new_arr.append({"typ": "puste", "start": 0, "end": arr_act[0].start})
        new_arr.append({"typ": arr_act[i].typ, "start": arr_act[i].start, "end": arr_act[i].end})

    new_act = Activity()
    new_act.start = 0
    new_act.end = 1
    new_act.typ = "Wylacznie kompa"

    # arr.append(new_act)

    return render_to_response('login/home.html', {'arr': new_arr, 'zmienna': "tutaj cos jest"})

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return HttpResponse('get response', {'tekst': 'get dziala'})
    if request.method == 'POST':
        zmienna = request.POST.get("powitanie", "")
        return HttpResponse('post response' + zmienna)
