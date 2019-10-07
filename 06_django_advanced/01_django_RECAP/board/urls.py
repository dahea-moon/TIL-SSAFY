from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.list, name='list'), # read 글 목록(list) render
    path('articles/<int:id>/', views.detail, name='detail'), # read 글 상세보기(detail) render
    
    path('articles/new/', views.new, name='new'), # create 글 쓰기(new) render
    path('articles/create/', views.create, name='create'), # create 글 저장(create)
    
    # path(''), # update 글 수정(edit) render
    # path(''), # update 글 실제수정(update)
    
    # path(''), # delete 글 삭제(delete)
]
