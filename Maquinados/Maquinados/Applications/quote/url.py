from django.urls import path

from .views import QuoteList, QuoteByClient, QuoteDetails, StatusQuoteList

urlpatterns = [
    path("", QuoteList.as_view()),
    path("<int:id>/", QuoteDetails),
    path("client/<str:nit>/", QuoteByClient),
    path("status/", StatusQuoteList.as_view())
]