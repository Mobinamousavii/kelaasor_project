from django.urls import path
from tickets.views import CreateTicketView, ReplyToTicketView, CloseTicketView, ListTicketView

urlpatterns = [
    path('create/', CreateTicketView.as_view()),
    path('<int:ticket_id>/reply/', ReplyToTicketView.as_view()),
    path('<int:pk>/close/',CloseTicketView.as_view()),
    path('list-ticket/', ListTicketView.as_view()),

]
