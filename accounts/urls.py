from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, RegisterView, profile, ChangePasswordView

# from .views import GeneratePdf

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    # path('pdf/', GeneratePdf.as_view(), name='certificate'),
]
