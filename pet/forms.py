from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import PetPost, RecommendPost, ShowoffPost

class PostForm(forms.ModelForm):
    class Meta:
        model = PetPost
        fields = ['title', 'thumnail', 'content', 'category']
        widgets = {
            'content' : SummernoteWidget(
                #attrs에 summernote에 대한 설정값들을 key/value 형식을 주면 된다.
                attrs={
                    'summernote': {
                    'width': '100%', 
                    'height': '400px',
                    'iframe': False,
                    'lang': 'ko-KR',
                    'codemirror': {
                        'mode': 'htmlmixed',
                    },
                }}
            ),
        }
        
#추천 폼
class RecommendPostForm(forms.ModelForm):
    class Meta:
        model = RecommendPost
        fields = ['title', 'thumnail', 'content', 'category']
        widgets = {
            'Recommend_content' : SummernoteWidget(
                #attrs에 summernote에 대한 설정값들을 key/value 형식을 주면 된다.
                attrs={
                    'summernote': {
                    'width': '100%', 
                    'height': '400px',
                    'iframe': False,
                    'lang': 'ko-KR',
                    'codemirror': {
                        'mode': 'htmlmixed',
                    },
                }}
            ),
        }


#내새끼 자랑 폼
class ShowoffPostForm(forms.ModelForm):
    class Meta:
        model = ShowoffPost
        fields = ['title','thumnail','content', 'category']
        widgets = {
            'ShowOff_content' : SummernoteWidget(
                #attrs에 summernote에 대한 설정값들을 key/value 형식을 주면 된다.
                attrs={
                    'summernote': {
                    'width': '100%', 
                    'height': '400px',
                    'iframe': False,
                    'lang': 'ko-KR',
                    'codemirror': {
                        'mode': 'htmlmixed',
                    },
                }}
            ),
        }