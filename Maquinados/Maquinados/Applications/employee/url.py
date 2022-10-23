from django.urls import path
from .views import EmployeeList, EmployeeDetails, EPSList

urlpatterns = [
    path("", EmployeeList.as_view()),
    path("<int:id>/",EmployeeDetails),
    path("eps/", EPSList.as_view())
]