from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)

class BaseRegistrationSerializer(ModelSerializer):
    def validate(self, data):
        event = data.get(self.Meta.event_field)  
        phone = data.get('phone')

        if event.status != 'registration_open':
            logger.warning(
                f"User with phone {phone} tried to register for '{event}' with status '{event.status}'"
            )
            raise serializers.ValidationError(
                "Registration is only allowed for items with 'registration_open' status."
            )

        model = self.Meta.model
        existing = model.objects.filter(
            **{self.Meta.event_field: event, 'phone': phone}
        )
        if existing.exists():
            logger.warning(
                f"Duplicate registration attempt by phone {phone} for event '{event}'"
            )
            raise serializers.ValidationError(
                "You have already submitted a request for this item."
            )

        return data