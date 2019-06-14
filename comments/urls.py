from comments.views import CommentsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', CommentsViewSet, basename='comments')


urlpatterns = router.urls
