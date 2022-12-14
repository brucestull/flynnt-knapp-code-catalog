from django.contrib.auth import get_user_model

from rest_framework import serializers

from code_catalog.models import Snippet, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'description'
        )


class SnippetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'description',
            'language',
            'author',
            'created',
            'updated',
            'tags'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
        )


# # GitHub Copilot created this class snippet.
# class SnippetSerializer(serializers.ModelSerializer):
#     tags = TagSerializer(many=True, read_only=True)

#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'description', 'language', 'author', 'created', 'updated', 'tags')

#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.language = validated_data.get('language', instance.language)
#         instance.author = validated_data.get('author', instance.author)
#         instance.created = validated_data.get('created', instance.created)
#         instance.updated = validated_data.get('updated', instance.updated)
#         instance.tags = validated_data.get('tags', instance.tags)
#         instance.save()
#         return instance