from django.urls import path

from .views import OrderByClient, OrderList, OrderDetail

urlpatterns = [
    path("", OrderList.as_view()),
    path("<int:id>/", OrderDetail),
    path("client/<str:nit>/", OrderByClient)
]