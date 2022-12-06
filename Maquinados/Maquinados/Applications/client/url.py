from django.urls import path
from .views import ClientDetail, ClientList, CountriesList, CitiesList, DepartmentList, DepartmentByCountry, CitiesByDeparment


urlpatterns = [
    path("", ClientList.as_view()),
    path("<int:id>/", ClientDetail),
    path("countries", CountriesList.as_view()),
    path("departments", DepartmentList.as_view()),
    path("departments/<int:id>", DepartmentByCountry),
    path("cities", CitiesList.as_view()),
    path("cities/<int:id>", CitiesByDeparment)
]
