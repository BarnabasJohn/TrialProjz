from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('', views.getRoutes, name='routes'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
