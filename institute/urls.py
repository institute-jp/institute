from django.urls import path
from . import views

app_name = "institute"   


urlpatterns = [
        path("register", views.register, name="register"),
        ]
