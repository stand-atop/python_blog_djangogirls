from django.urls import path
from . import views
# path, blog app에서 사용할 모든 views를 가져옴

# post_list라는 view가 루트 URL(http://127.0.0.1:8000/)에 할당됨
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
