from django.contrib.auth import get_user_model

from rest_framework import viewsets, generics

from code_catalog.models import Snippet, Tag
from api import serializers


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all().filter(id=self.request.user.id)


# class CurrentUserView(generics.RetrieveAPIView):
#     serializer_class = serializers.UserSerializer

#     def get_object(self):
#         print('self.request.user: ', self.request.user)
#         return self.request.user