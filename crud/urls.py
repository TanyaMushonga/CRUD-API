from django.urls import path, include
from .views import RegisterAPI, LoginAPI, LogoutAPI, AuthorViewSet, BookViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')

urlpatterns = router.urls + [
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', LogoutAPI.as_view(), name='logout'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]