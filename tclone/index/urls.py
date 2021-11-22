from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('delete/<int:tweet_id>', views.delete, name='delete'), # この行を追加
    path('update/<int:tweet_id>', views.update, name='update'), # この行を追加
    path('like/<int:tweet_id>', views.like, name='like'), #ここを追加
]