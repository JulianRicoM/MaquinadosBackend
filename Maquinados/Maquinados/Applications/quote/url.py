from django.urls import path

from .views import QuoteList, QuoteByClient, QuoteDetails

urlpatterns = [
    path("", QuoteList.as_view()),
    path("<int:id>/", QuoteDetails),
    path("client/<str:nit>", QuoteByClient)
]