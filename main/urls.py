from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("authenticate/", views.login),
    # path("user/", views.MeView.as_view()),
]