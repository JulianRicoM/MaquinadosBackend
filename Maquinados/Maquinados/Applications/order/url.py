from django.urls import path

from .views import OrderByClient, createOrder, OrderDetail, ListOrder, getOrderProcess

urlpatterns = [
    path("", createOrder),
    path("list", ListOrder),
    path("<int:id>/", OrderDetail),
    path("process", getOrderProcess ),
    path("client/<str:nit>/", OrderByClient),
]