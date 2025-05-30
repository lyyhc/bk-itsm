# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # 登录获取token
    TokenRefreshView,     # 刷新token
)
from .views import HelloView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
]
