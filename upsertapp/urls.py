from django.urls import path
from . import views

urlpatterns = [
    path("upsert/", views.upsert),
]
