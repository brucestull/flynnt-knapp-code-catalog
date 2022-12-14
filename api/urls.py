from django.urls import path

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('snippets', views.SnippetViewSet, basename='snippettt')
router.register('tags', views.TagViewSet, basename='taggg')
router.register('users', views.UserViewSet, basename='userrr')
router.register('current-user', views.CurrentUserViewSet, basename='currentuserrr')

urlpatterns = router.urls + [
    # path('current-user/', views.CurrentUserViewSet.as_view({'get': 'list'}), name='current_user'),
    # path('current-user/', views.CurrentUserView.as_view(), name='current_user')
]