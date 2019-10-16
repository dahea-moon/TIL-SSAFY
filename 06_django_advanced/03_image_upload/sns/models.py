from django.db import models
from django.urls import reverse

# 지우고 싶을때
"""
$ python manage.py migrate <APP_NAME> zero  => unapplying all migrations
$ rm <APP_NAME>/migrations/0* => deleting all migrations files except __init__.py (all migrations files starting with 0)
"""

class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True) # 반드시 pip install Pillow 
    created_at = models.DateTimeField(auto_now_add=True)
    # auto now add 는 추가되었을 때, 생성 되었을 때 시간을 잼
    updated_at = models.DateTimeField(auto_now=True)
    # 수정 세이브 될 때 마다 시간을 잼

    # detail 페이지를 쓸 거라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.id})

    def __str__(self):
        return f'{self.id}: {self.content[:10]}'
