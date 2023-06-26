from rest_framework import serializers

from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    ower = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'ower', 'create_time']



class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'ower', 'content_html', 'create_time']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'create_time']
