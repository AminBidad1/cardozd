from backend.srvs.camp.camp.models import Post
from backend.srvs.camp.camp.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering = ["-created_at"]
