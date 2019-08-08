from django.urls import path
from . import views

urlpatterns = [
    # READ
    path('articles/', views.index),
    path('articles/<int:article_id>/', views.show),
    # Create
    path('articles/new/', views.new),
    path('articles/create/', views.create),
    # Update
    path('articles/<int:article_id>/edit/', views.edit),
    path('articles/<int:article_id>/update/', views.update),
    # Delete
    path('articles/<int:article_id>/delete/', views.delete),
]
