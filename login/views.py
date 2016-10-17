from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def index(request):
    arr = ['akt']
    return render_to_response('login/home.html', {'arr': arr, 'zmienna': "tutaj cos jest"})

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return HttpResponse('get response', {'tekst': 'get dziala'})
    if request.method == 'POST':
        zmienna = request.POST.get("powitanie", "")
        return HttpResponse('post response' + zmienna)
