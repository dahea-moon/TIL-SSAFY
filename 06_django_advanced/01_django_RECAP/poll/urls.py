from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('<int:question_id>/', views.poll_detail, name='poll_detail'),
    path('<int:question_id>/<int:choice_id>', views.upvote, name='upvote'),
]
