from django.urls import path
from .views import EmployeeList, EmployeeDetails, EPSList, CreateEmployee, PositionList

urlpatterns = [
    path("list/", EmployeeList),
    path("<int:id>/",EmployeeDetails),
    path("eps/", EPSList.as_view()),
    path("", CreateEmployee),
    path("position/", PositionList.as_view()),
    
]   