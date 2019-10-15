from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('', views.index, name='index'),
    path('articles/', views.list_article, name='list_article'), # read 글 목록(list) render
    path('articles/<int:article_id>/', views.detail_article, name='detail_article'), # read 글 상세보기(detail) render
    path('articles/new/', views.new_article, name='new_article'), # create 글 쓰기(new) render
    # path('articles/create/', views.create, name='create'), # create 글 저장(create)
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'), # update 글 수정(edit) render
    # path('articles/<int:id>/update/', views.update, name='update'), # update 글 실제수정(update)
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'), # delete 글 삭제(delete)
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),
    path('articles/<int:article_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
