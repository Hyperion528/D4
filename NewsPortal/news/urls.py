from django.urls import path
from .views import New, NewDetailView, News, news_list, NewCreateView, NewUpdateView, NewDeleteView


 
urlpatterns = [
    path('', News.as_view()),
    path('<int:pk>', NewDetailView.as_view(), name='new_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search', news_list),
    path('add/', NewCreateView.as_view(), name='new_add'),
    path('edit/<int:pk>', NewUpdateView.as_view(), name='new_edit'),
    path('delete/<int:pk>', NewDeleteView.as_view(), name='new_delete'),
]