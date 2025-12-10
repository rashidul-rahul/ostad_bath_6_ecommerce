from django.urls import path
from .views import RegisterView, LoginView, LogoutView, SendResetEamil, ResetPassword

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('send-email/', SendResetEamil.as_view(), name='send_reset'),
    path('reset-password/<uuid:token>/', ResetPassword.as_view(), name='reset_password')
]
