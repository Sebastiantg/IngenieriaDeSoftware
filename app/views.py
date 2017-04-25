from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    page = "<h1 align='center'> hola mundo! </h1>"
    return HttpResponse(page)


def base(request):
    return render(request, "base.html")
