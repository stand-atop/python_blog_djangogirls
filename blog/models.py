from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model): #모델정의
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey: 다른 모델에 대한 링크
    title = models.CharField(max_length=200) # CharField: 200자로 제한된 텍스트
    text = models.TextField() # TextField: 글자 수 제한이 없는 긴텍스트
    created_date = models.DateTimeField( # DateTimeField: 날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title # Post모델의 제목
