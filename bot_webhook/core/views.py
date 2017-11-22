from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, "index.html")


@csrf_exempt
def event(requests):
    print(requests.body)
    return JsonResponse({'status': 'true', 'message': 'worked'})
    # return HttpResponse()