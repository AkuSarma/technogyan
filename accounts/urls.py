from django.urls import path
from .views import SignUpView, ProfileView

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name = 'signup'),
    path('profile/', ProfileView.as_view(), name="profile"),
]