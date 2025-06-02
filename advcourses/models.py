from django.db import models
from bootcamps.base import BaseCourse, BaseCourseUser, BaseCourseRegistration

class AdvCourse(BaseCourse):
    platform_name = models.CharField(max_length=100)
    is_live = models.BooleanField(default=False)
    access_instructions = models.TextField(blank=True) 

class AdvCourseUser(BaseCourseUser):
    advcourse = models.ForeignKey(AdvCourse, on_delete=models.CASCADE, related_name='members')
    class Meta(BaseCourseUser.Meta):
        unique_together = ('advcourse', 'user')

    def __str__(self):
        return f'{self.user.phone} - {self.role} - {self.advcourse.title}'
    
class AdvCourseRegistration(BaseCourseRegistration):
    advcourse = models.ForeignKey(AdvCourse, on_delete=models.CASCADE, related_name='registration_requests')

    def __str__(self):
        return f'{self.full_name} - {self.advcourse.title}'


