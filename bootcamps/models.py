from django.db import models
from django.conf import settings
from bootcamps.base import BaseCourse , BaseCourseUser, BaseCourseRegistration

class Bootcamp(BaseCourse):
    location = models.CharField(max_length=200, blank=True)

class BootcampUser(BaseCourseUser):
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, related_name='members')
    class Meta:
        unique_together = ('bootcamp', 'user')

    def __str__(self):
        return f'{self.user.phone} - {self.role} - {self.bootcamp.title}'
    
    
class BootcampRegistration(BaseCourseRegistration):
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, related_name='registration_requests')

    def __str__(self):
        return f'{self.full_name} - {self.bootcamp.title}'
    