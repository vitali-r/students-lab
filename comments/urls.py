from comments.views import CommentsViewSet
from django.conf.urls import url


urlpatterns = [
    url(r'list', CommentsViewSet.as_view({'get': 'list'}), name='comments-list'),
    url(r'add', CommentsViewSet.as_view({'post': 'create'}), name='add-comment')
]
