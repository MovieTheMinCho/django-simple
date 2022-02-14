from django.http import JsonResponse
from django.views import View
from board.models import Article
from django.utils import timezone

class MyApiView(View):
    def get(self, request):
        try:
            start = int(request.GET.get('start'))
            size = int(request.GET.get('size'))
            articles = Article.objects.order_by('-date')
            data = []
            for article in articles[start:start+size]:
                data.append({
                    'title':article.title,
                    'content':article.content,
                    'author':article.author,
                    'date':article.date
                    })

            return JsonResponse({'result':'success', 'data':data}, status=200)
        except:
            return JsonResponse({'result':'fail'}, status=400)

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

