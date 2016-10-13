from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse


@csrf_exempt
def index(request):
    klik = 'eloszka'
    if request.method == 'POST':
        # if 'klik' in request.POST:

        klik = 'dziala'
    return render(request, 'login/home.html', {'klik': klik})
