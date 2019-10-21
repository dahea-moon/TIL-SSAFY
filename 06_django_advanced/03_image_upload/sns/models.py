from django.db import models
from django.urls import reverse
from django.conf import settings
from faker import Faker

f = Faker()

# 지우고 싶을때
"""
$ python manage.py migrate <APP_NAME> zero  => unapplying all migrations
$ rm <APP_NAME>/migrations/0* => deleting all migrations files except __init__.py (all migrations files starting with 0)
"""


class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_postings', blank=True)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # 반드시 pip install Pillow 
    created_at = models.DateTimeField(auto_now_add=True)
    # auto now add 는 추가되었을 때, 생성 되었을 때 시간을 잼
    updated_at = models.DateTimeField(auto_now=True)
    # 수정 세이브 될 때 마다 시간을 잼

    class Meta:
        ordering = ['-created_at',] # created_at을 내림차순으로 정렬

    # detail 페이지를 쓸 거라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.id})

    def __str__(self):
        return f'{self.id}: {self.content[:10]}'

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                content=f.sentence(),
                icon='fas fa-angrycreative',
            )


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # related_name 이 없으면, posting.comment_set / 아래와 같다면, posting.comments
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return f'{self.id}: {self.content[:10]}'


    @classmethod
    def dummy(cls, n, posting_id):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                posting_id=posting_id,
                content=f.sentence(),
            )
