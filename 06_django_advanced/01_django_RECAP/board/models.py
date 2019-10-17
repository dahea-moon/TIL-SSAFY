from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self): # detail page가 있을 때
        return reverse("board:detail_article", kwargs={"article_id": self.id})


class Comment(models.Model):
    content = models.CharField(max_length=200) # 200 넘어가면 알아서 자르고 저장
    # 폭포 처럼 ORIGINAL KEY(여기서는 CLASS ARTICLE)이 사라지면 여기서도 ARTICLE이 사라짐
    article = models.ForeignKey(Article, on_delete=models.CASCADE)