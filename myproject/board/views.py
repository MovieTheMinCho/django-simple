from django.http import JsonResponse
from django.views import View

class MyApiView(View):
    def get(self, request):
        try:
            name = request.GET.get('name')
            old = request.GET.get('old')
            return JsonResponse({'name':name, 'old':old}, status=200)
        except:
            return JsonResponse({'post-error':'err'}, status=400)

    def post(self, request):
        print(request.POST)
        try:
            name = request.POST.get('name')
            return JsonResponse({'name':name}, status=200)
        except:
            return JsonResponse({'post-error':'err'},status=400)

