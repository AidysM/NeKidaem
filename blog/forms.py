from django.db.models import fields
from django.forms import ModelForm, Textarea, Select
from django.forms import widgets   # Импортируем true-false поле
from .models import Post
from django.contrib.auth.models import User


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля.
    # Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['title', 'text']
        # widgets = {
        #     # "adv_name": Char(attrs={"class": "form-control"}),
        #     "category": Select(choices=Category.objects.all(), attrs={"class": "form-control"}),
        #     # "image": Image(attrs={"class": "form-control"}),
        #     "content": Textarea(attrs={"class": "form-control"}),
        #     "announcer": Select(choices=Announcer.objects.all(), attrs={"class": "form-control"}),
        # }


# class ReplyForm(ModelForm):
#     class Meta:
#         model = Reply
#         fields = ('user', 'advert', 'text')
#         widgets = {
#             "user": Select(choices=User.objects.all(), attrs={"class": "form-control"}),
#             "advert": Select(choices=Advert.objects.all(), attrs={"class": "form-control"}),
#             "text": Textarea(attrs={"class": "form-control"})
#         }

