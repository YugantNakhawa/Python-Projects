
from django.urls import path
from .views import SignUpView, logout_view

urlpatterns = [
    path('accounts/', SignUpView.as_view(), name = 'signup'),
    path('logout/', logout_view, name='logout_view'),  # Add this line for logout URL
]