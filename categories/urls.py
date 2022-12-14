from django.urls import path, include
from rest_framework.routers import SimpleRouter

from categories import views

router = SimpleRouter()
router.register(r'', views.CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
]