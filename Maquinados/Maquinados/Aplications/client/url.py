from django.urls import path
from .views import ClientDetail, ClientList


urlpatterns = [
    path("", ClientList.as_view()),
    path("<int:id>/", ClientDetail)
]