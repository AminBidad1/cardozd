from rest_framework import serializers

from backend.srvs.camp.camp.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.URLField(
        allow_null=False,
        allow_blank=False,
    )

    class Meta:
        model = Post
        fields = '__all__'
