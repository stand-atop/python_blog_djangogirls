from django.shortcuts import render

# 요청(request)을 받아 render메서드를 호출해 blog/post_list.html 템플릿을 보여주는 함수
def post_list(request):
        return render(request, 'blog/post_list.html', {})

        
