from django.urls import path
from . import views

urlpatterns = [
    # utiles/cube/<int>/ * 슬래쉬 => 앞x뒤o
    path('cube/<int:num>/', views.cube),
    path('check_int/<int:num>/', views.check_int),
    path('pick_lotto/', views.pick_lotto)
]
