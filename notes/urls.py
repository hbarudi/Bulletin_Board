from django.urls import path
from . import views

# This list handles specific pages like /post/1 or /post/new
urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("post/<int:pk>/", views.note_detail, name="note_detail"),
    path("post/new/", views.note_create, name="note_create"),
    path("post/<int:pk>/edit/", views.note_update, name="note_update"),
    path("post/<int:pk>/delete/", views.note_delete, name="note_delete"),
]
