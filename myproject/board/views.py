from django.http import HttpResponse
import json

def index(request):
    dic = {'a': 1, 'b': 2, 'c': 3}
    return HttpResponse(json.dumps(dic));
