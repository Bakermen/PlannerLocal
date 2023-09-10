from django.urls import path
from .views import *

app_name = "jobs"

urlpatterns = [
    path("", ApplicataionCreateAndListView.as_view(), name="list"),
    path("application/<int:pk>", ApplicationDetailView.as_view(), name="application"),
    path("application/<int:pk>/edit/", ApplicationUpdateView.as_view(), name="update"),
    path(
        "application/<int:pk>/delete/", ApplicationDeleteView.as_view(), name="delete"
    ),
]
