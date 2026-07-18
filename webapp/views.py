from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def main_view(request):
    return render(request ,'index.html')