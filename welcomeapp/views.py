from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    res = HttpResponse("""<html><body><h1>Welcome Home</h1></body></html>""")
    return res