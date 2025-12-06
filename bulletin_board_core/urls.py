# Hashem Barudi
# Urls to access web app from web browser.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
# This line says: "For the homepage go look at notes/urls.py"
    path("", include("notes.urls")),
]
