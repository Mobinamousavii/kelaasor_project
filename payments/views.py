from rest_framework.generics import CreateAPIView, ListAPIView
from payments.serializers import InvoiceSerializer, PaymentSerializer
from payments.models import Invoice, Payment
from accounts.permissions import HasRole
from django.shortcuts import get_object_or_404
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

class CreateInvoiceView(CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [HasRole('financial')]

    def perform_create(self, serializer):
        user_id = self.request.data.get("user")
        user = get_object_or_404(User, id=user_id)
        serializer.save(user=user)

class MyInvoicesView(ListAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user).order_by('-created_at')

class CreatePaymentView(CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        invoice = serializer.validated_data['invoice']

        if invoice.user != self.request.user:
            raise ValidationError("You are not allowed to pay for this invoice.")

        serializer.save()



