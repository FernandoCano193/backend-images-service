from django.urls import path
from . import views

urlpatterns = [
    path("api/files/upload/direct/start/", views.upload_start, name="upload_start"),
    path("api/files/upload/direct/finish/", views.upload_finish, name="upload_finish"),
]