from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete-task/<int:pk>", views.deletePage, name="deletepage"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("edit/<int:pk>", views.editPage, name="edit"),
    path("toggle_done/<int:task_id>/", views.toggleDone, name="toggle_done"),
]
