from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from tickets.serializers import TicketSerializer, TicketMessageSerializer
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket, TicketMessage
from bootcamps.models import Bootcamp
from advcourses.models import AdvCourse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from accounts.permissions import HasRole
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

class CreateTicketView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=self.request.user)
        related_bootcamp = self.request.data.get('related_bootcamp')
        related_advcourse = self.request.data.get('related_advcourse')

        if not related_advcourse and not related_advcourse:
            user_bootcamp = Bootcamp.objects.filter(members__user = user)
            user_adv = AdvCourse.objects.filter(members__user = user)

            if user_bootcamp.count() == 1:
                serializer.save(user=user, related_bootcamp=user_bootcamp.first())
            elif user_adv.count() == 1:
                serializer.save(user=user, related_advcourse=user_adv.first())
            else:
                serializer.save(user=user)
        
        else:
            serializer.save(user=user)


class ReplyToTicketView(CreateAPIView):
    serializer_class = TicketMessageSerializer
    permission_classes = [HasRole('support')]

    def perform_create(self, serializer):
        ticket_id = self.kwargs.get('ticket_id')
        ticket = get_object_or_404(Ticket, id=ticket_id)

        if ticket.status == 'closed':
            raise ValidationError("This ticket is already closed and cannot be replied to.")

        serializer.save(ticket=ticket, sender=self.request.user)

        if ticket.status in ['pending', 'reviewing']:
            ticket.status = 'answered'
            ticket.save()


class CloseTicketView(UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [HasRole('support')]

    def update(self, request, *args, **kwargs):
        ticket = self.get_object()

        if ticket.status == 'closed':
            return Response({"detail": "This ticket is already closed."}, status=status.HTTP_400_BAD_REQUEST)
        
        ticket.status = 'closed'
        ticket.save()

        return Response({"detail": "Ticket has been successfully closed."}, status=status.HTTP_200_OK)


class ListTicketView(ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [HasRole('support')]

    def get_queryset(self):
        return Ticket.objects.all().order_by('-created_at')
    
class MyTicketsView(ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user).order_by('-created_at')
    


