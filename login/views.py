from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Activity
import datetime


def dt_to_num(dataczas):
    return ((dataczas.hour + dataczas.minute / 60) - 8) / 10


def dt_to_hour(dataczas):
    return str(dataczas.hour) + ":" + str(dataczas.minute)


@csrf_exempt
def index(request):

    now = datetime.datetime.now()
    # now.weekday() - 0 = monday, 6 = sunday

    arr_act = Activity.objects.filter(start__date=datetime.datetime(2016, 10, 18))
    arr_act.order_by('start')
    new_arr = list()
    kalendarz = list()

    for i in range(0, arr_act.count()):
        if i == 0:
            new_arr.append({"typ": "puste",
                            "klasa": "puste",
                            "start": "8:00",
                            "end": dt_to_hour(arr_act[0].start),
                            "dur": dt_to_num(arr_act[0].start) * 800
                            })
        new_arr.append({"typ": arr_act[i].typ,
                        "klasa": "pelne",
                        "start": dt_to_hour(arr_act[i].start),
                        "end": dt_to_hour(arr_act[i].end),
                        "dur": (dt_to_num(arr_act[i].end) - dt_to_num(arr_act[i].start)) * 800
                        })
        if i != arr_act.count() - 1:
            new_arr.append({"typ": "puste",
                            "klasa": "puste",
                            "start": dt_to_hour(arr_act[i].end),
                            "end": dt_to_hour(arr_act[i + 1].start),
                            "dur": (dt_to_num(arr_act[i + 1].start) - dt_to_num(arr_act[i].end)) * 800
                            })
        else:
            new_arr.append({"typ": "puste",
                            "klasa": "puste",
                            "start": dt_to_hour(arr_act[i].end),
                            "end": "18:00",
                            "dur": (1 - dt_to_num(arr_act[i].end)) * 800
                            })

    return render_to_response('login/main.html', {'arr': new_arr, 'zmienna': "tutaj cos jest"})

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return HttpResponse('get response', {'tekst': 'get dziala'})
    if request.method == 'POST':
        zmienna = request.POST.get("powitanie", "")
        return HttpResponse('post response' + zmienna)
