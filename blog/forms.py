from django import forms
from .models import Post

#PostFrom 만들 폼 이름, 장고에 만들 form 이 ModelForms 라고 알려
class PostForm(forms.ModelForm):

    class Meta:
        #이 폼을 만들기 위해 어떤 model이 쓰여야 하는지 알려줌
        model = Post
        #이 폼 필드
        fields = ('title', 'text',)
