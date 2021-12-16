from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:pk>', views.blog_detail, name='blog-detail')
]