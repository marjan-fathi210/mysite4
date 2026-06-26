from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse('<h1>This is a test</h1>')
def json_test(request):
    return JsonResponse({'name': 'marjan'})
