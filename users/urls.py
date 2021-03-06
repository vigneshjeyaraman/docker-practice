"""
    Urls to handle user operations.
"""
from django.urls import path
from users import views


urlpatterns = [
    path('signup', views.Signup.as_view({"post":"create"}), name='signup'),
    path('login', views.Login.as_view({"post":"create"}), name='login'),
]