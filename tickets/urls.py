from django.urls import path
from tickets.views import CreateTicketView

urlpatterns = [
    path('create/', CreateTicketView.as_view()),
]
