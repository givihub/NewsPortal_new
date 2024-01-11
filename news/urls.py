from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SubscriberView
from django.views.decorators.cache import cache_page

urlpatterns = [
#   path('', PostList.as_view(), name='post_list'), #http://127.0.0.1:8000/news/
#   path('<int:pk>', PostDetail.as_view(), name='post_detail'), #http://127.0.0.1:8000/1
   path('create/', PostCreate.as_view(), name='post_create'), #http://127.0.0.1:8000/news/create/
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'), #http://127.0.0.1:8000/news/pk/update/
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'), #http://127.0.0.1:8000/news/pk/delete/
   path('post/', SubscriberView.as_view(), name='subscribe'), #http://127.0.0.1:8000/
   path('<int:pk>/', cache_page(300)(PostDetail.as_view()), name='post_detail'), #кэширование страниц с новостями 5 минут
   path('', cache_page(60)(PostList.as_view()), name='post_list'), #кэширование главной страницы 1 минута
]