from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 내가 머라고 접근할지 = ...related_name= 남이 나를 뭐라고 부를지
    like_users = models.ManyToManyField(User, related_name='like_articles')

