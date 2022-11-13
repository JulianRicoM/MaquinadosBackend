from django.urls import path

from .views import ToolList, ToolDetails

urlpatterns = [
    path("", ToolList.as_view()),
    path("<int:id>/", ToolDetails)
]