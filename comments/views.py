from rest_framework import viewsets
from comments.serializers import CommentsSerializer
from comments.models import Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
