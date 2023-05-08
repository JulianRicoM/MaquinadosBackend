from django.urls import path

from .views import ToolList, ToolDetails, Status

urlpatterns = [
    path("", ToolList.as_view()),
    path("<int:id>/", ToolDetails),
    path("status/", Status.as_view())
]