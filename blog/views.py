from django.shortcuts import render
from django.utils import timezone
from .models import Post


# 요청(request)을 받아 render메서드를 호출해 blog/post_list.html 템플릿을 보여주는 함수
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})
