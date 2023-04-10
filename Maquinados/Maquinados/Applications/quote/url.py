from django.urls import path

from .views import CreateQuote, ListQuote, QuoteByClient, QuoteDetails, StatusQuoteList

urlpatterns = [
    path("", CreateQuote),
    path("<int:id>/", QuoteDetails),
    path("list", ListQuote),
    path("client/<str:nit>/", QuoteByClient),
    path("status/", StatusQuoteList.as_view())
]