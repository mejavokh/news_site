from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('category/<int:category_id>/', news_by_categories, name='news_by_categories'),
    path('create_news/', NewsPostCreateView.as_view(), name='create_news'),
    path('news_detail/<int:pk>/', DetailNewsView.as_view(), name='news_detail'),
    path('comment/<int:pk>/', CreateCommentView.as_view(), name='create_comment')
]



