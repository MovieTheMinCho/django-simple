from django.http import JsonResponse
from django.views import View

class MyApiView(View):
    def get(self, request):
        try:
            name = request.GET.get('name')
            old = request.GET.get('old')
            return JsonResponse({'name':name, 'old':old}, status=200)
        except:
            JsonResponse({'error':'err'}, status=400)

