from django.http import JsonResponse
from django.views import View
from board.models import Article
from django.utils import timezone

class MyApiView(View):
    def get(self, request):
        try:
            name = request.GET.get('name')
            old = request.GET.get('old')
            return JsonResponse({'name':name, 'old':old}, status=200)
        except:
            return JsonResponse({'post-error':'err'}, status=400)

    def post(self, request):
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            author = request.POST.get('author')
            article = Article(date=timezone.now(), title=title, content=content, author=author)
            article.save()
            return JsonResponse({'result':'success'}, status=200)
        except:
            return JsonResponse({'result':'fail'},status=400)

