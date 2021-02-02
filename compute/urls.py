from django.urls import path
from compute import views

urlpatterns = [
    path("", views.home),
    path("sleep/<int:second>", views.sleep),
    path("sleep/", views.sleep, {"second": 5}),
]
