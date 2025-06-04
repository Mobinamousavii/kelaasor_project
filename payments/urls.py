from django.urls import path
from payments.views import CreateInvoiceView, MyInvoicesView, CreatePaymentView, ConfirmPaymentView

urlpatterns = [
    path('invoice/create/', CreateInvoiceView.as_view()),
    path('my-payments/', MyInvoicesView.as_view()),
    path('create/', CreatePaymentView.as_view()),
    path('<int:pk>/confirm/', ConfirmPaymentView.as_view()),
]
