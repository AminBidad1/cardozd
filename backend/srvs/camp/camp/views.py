from backend.srvs.camp.camp.models import (
    Post,
    CompanyPage,
)
from backend.srvs.camp.camp.serializers import (
    PostSerializer,
    CompanyPageSerializer,
)
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering = ["-created_at"]


class CompanyPageViewSet(ModelViewSet):
    queryset = CompanyPage.objects.all()
    serializer_class = CompanyPageSerializer
    ordering = ["-created_at"]
