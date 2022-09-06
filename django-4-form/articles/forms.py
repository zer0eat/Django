# articles/forms.py

from tkinter import Widget
from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     NATION_A = 'KR'
#     NATION_B = 'CH'
#     NATION_C = 'JP'
#     NATION_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices = NATION_CHOICES)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TimeInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        )
    )

    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content',
                'placeholder' : 'Enter the content',
                'row' : 5,
                'col' : 50,
            }
        ),
        error_messages={
            'required' : '내용 입력좀',
        }
    )
    
    class Meta:
        model = Article  # 어떤 모델을 기반으로 할지
        fields = '__all__' # 어떤 모델필드 중 어떤 것을 출력할지 / ('title', 'content')와 같은 의미
        