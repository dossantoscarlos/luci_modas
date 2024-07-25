# example/views.py

from django.http import HttpResponse

def index(request):
    arr = []
    for i in range(0,100):
        arr.append(i)

    return HttpResponse(arr)