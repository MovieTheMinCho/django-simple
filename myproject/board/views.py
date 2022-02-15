from django.http import JsonResponse
from django.views import View
from board.models import Article
from django.utils import timezone
from django.http import QueryDict


FAIL = JsonResponse({'result':'fail'}, status=400)

class MyApiView(View):
    def get(self, request):
        try:
            data=[]
            start = int(request.GET.get('start', default=0))
            size = int(request.GET.get('size', default=10))
            articles = Article.objects.order_by('-date')
            for article in articles[start:start+size]:
                data.append(article.get_dict())
            return JsonResponse({'result':'success', 'data':data}, status=200)
        except:
            return FAIL

    def post(self, request):
        try:
            title = request.POST.get('title')[:30]
            content = request.POST.get('content')[:1500]
            author = request.POST.get('author')[:10]
            password = request.POST.get('password')[:10]
            article = Article(
                    date=timezone.now(),
                    title=title,
                    content=content,
                    author=author,
                    password=password)
            article.save()
            return JsonResponse({'result':'success'}, status=200)
        except:
            return FAIL

class IdApiView(View):
    def get(self, request, article_id):
        try:
            article = Article.objects.get(id_number=article_id)
            return JsonResponse(
                    {
                        'result':'success',
                        'data':article.get_dict()
                        }, status=200)
        except:
            return FAIL

    def post(self, request, article_id):
        try:
            article = Article.objects.get(id_number=article_id)
            if article.password == request.POST.get('password')[:10]:
                article.delete()
            else:
                return JsonResponse({
                    'result':'success',
                    'delete':'wrong password'}, status=301)
            return JsonResponse({
                'result':'success',
                'delete':'success'}, status=301)
        except:
            return FAIL




