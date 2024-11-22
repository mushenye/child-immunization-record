from django.urls import path 
from . views import (
        LoginView, 
        LogoutView, 
        MyTokenObtainPairView, 
        Register )

from rest_framework_simplejwt.views import (
    TokenRefreshView, 
    TokenVerifyView
    )




urlpatterns = [

    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]




