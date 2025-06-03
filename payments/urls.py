from django.urls import path
from payments.views import CreateInvoiceView, MyInvoicesView, CreatePaymentView

urlpatterns = [
    path('invoice/create/', CreateInvoiceView.as_view()),
    path('my-payments/', MyInvoicesView.as_view()),
    path('create/', CreatePaymentView.as_view()),
]
