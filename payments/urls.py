from django.urls import path
from payments.views import CreateInvoiceView, MyInvoicesView

urlpatterns = [
    path('create/', CreateInvoiceView.as_view()),
    path('my-payments/', MyInvoicesView.as_view()),
    

]
