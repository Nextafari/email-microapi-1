from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.get_user_profile, name="get_user_profile"),
]