from rest_framework import serializers

from backend.srvs.camp.camp.models import (
    Post,
    CompanyPage,
)


class PostSerializer(serializers.ModelSerializer):
    url = serializers.URLField(
        allow_null=False,
        allow_blank=False,
    )
    company = serializers.PrimaryKeyRelatedField(
        queryset=CompanyPage.objects.all(),
        many=False,
    )

    class Meta:
        model = Post
        fields = '__all__'


class CompanyPageSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = CompanyPage
        fields = "__all__"
