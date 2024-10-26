from django.http import HttpResponseRedirect as redirect
from django.http import HttpRequest
from django.shortcuts import render

def check_file_exists(request : HttpRequest):
    return redirect(redirect_to="/admin")

def index(request : HttpRequest):
    return render(request=request, template_name="index.html") 