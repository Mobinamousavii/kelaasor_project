from rest_framework.generics import CreateAPIView
from tickets.serializers import TicketSerializer, TicketMessageSerializer
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket, TicketMessage
from bootcamps.models import Bootcamp
from advcourses.models import AdvCourse
from rest_framework import status
from rest_framework.exceptions import ValidationError

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
                raise ValidationError("Please specify which course this ticket is related to.")
        
        else:
            serializer.save(user=user)

            