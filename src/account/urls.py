from django.urls import path,re_path
from . import views
from django.conf.urls import include
from rest_framework import routers
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

router = routers.DefaultRouter()



urlpatterns = [
    re_path('', include(router.urls)),

    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
    
]