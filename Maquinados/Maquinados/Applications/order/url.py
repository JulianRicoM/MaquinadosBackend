from django.urls import path

from .views import OrderByClient, createOrder, OrderDetail, ListOrder, getOrderProcess, PaymentMethods, Currencies

urlpatterns = [
    path("", createOrder),
    path("list", ListOrder),
    path("<int:id>/", OrderDetail),
    path("process", getOrderProcess ),
    path("client/<str:nit>/", OrderByClient),
    path("payment", PaymentMethods),
    path("currencies", Currencies)
]