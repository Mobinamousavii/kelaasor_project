from django.urls import path
from payments.views import CreateInvoiceView

urlpatterns = [
    path('create/', CreateInvoiceView.as_view()),
]
