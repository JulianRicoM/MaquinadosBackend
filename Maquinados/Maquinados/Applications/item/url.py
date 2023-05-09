from django.urls import path
from .views import ItemList, ItemDetails, MaterialList, Measurement

urlpatterns = [
    path("", ItemList.as_view()),
    path("<int:id>/", ItemDetails),
    path("material", MaterialList.as_view()),
    path("measurement", Measurement.as_view())
]