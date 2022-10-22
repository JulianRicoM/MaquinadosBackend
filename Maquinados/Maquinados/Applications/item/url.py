from django.urls import path
from .views import ItemList, ItemDetails

urlpatterns = [
    path("", ItemList.as_view()),
    path("<int:id>/", ItemDetails)
]