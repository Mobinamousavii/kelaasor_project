from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from payments.serializers import InvoiceSerializer, PaymentSerializer
from payments.models import Invoice, Payment
from accounts.permissions import HasRole
from django.shortcuts import get_object_or_404
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

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

class ConfirmPaymentView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [HasRole('financial')]  

    def update(self, request, *args, **kwargs):
        payment = self.get_object()
        invoice = payment.invoice

        if invoice.status == 'paid':
            return Response({'detail': 'This invoice is already marked as paid.'}, status=status.HTTP_400_BAD_REQUEST)


        total_paid = sum(p.amount for p in invoice.payments.all()) + payment.amount

        if total_paid >= invoice.amount:
            invoice.status = 'paid'
        else:
            invoice.status = 'pending_review'

        invoice.save()

        return Response({'detail': 'Payment confirmed and invoice updated.'}, status=status.HTTP_200_OK)



