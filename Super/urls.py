from django.urls import path
from . import views


urlpatterns =[
path('', views.get_all_supers),
path('<int:pk>/', views.super_detail)
]