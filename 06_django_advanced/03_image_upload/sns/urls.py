from django.urls import path
from . import views

app_name = 'sns'

urlpatterns = [
    path('newsfeed/', views.posting_list, name='posting_list'),
    path('postings/<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('postings/create/', views.create_posting, name='create_posting'),
    path('<int:posting_id>/delete/', views.delete_posting, name='delete_posting'),
    path('postings/<int:posting_id>/comment/', views.create_comment, name='create_comment'),
    path('<int:posting_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment')
]
