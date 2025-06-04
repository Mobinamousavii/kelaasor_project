from django.db import models
from django.conf import settings

class BaseCourse(models.Model):
    """
    Abstract base model for course-like objects.

    Includes fields common to both Bootcamp and AdvCourse:
    - title: Title of the course
    - description: Short summary of the course
    - start_date & end_date: Duration of the course
    - capacity: Maximum number of participants
    - status: Workflow stage (draft, open for registration, etc.)
    - price: Course fee
    """

    STATUS_CHOICES = (
        ('draft', 'پیش‌نویس'),
        ('registration_open', 'در حال ثبت‌نام'),
        ('in_progress', 'در حال برگزاری'),
        ('completed', 'برگزار شده'),
        ('canceled', 'لغو شده'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default= 'draft')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class BaseCourseUser(models.Model):
    """
    Abstract base model for users enrolled in a course.

    Fields:
    - user: The user who joined the course
    - role: Role of the user in the course (student, mentor, teacher)
    - joined_at: When the user was added
    """
    ROLE_CHOICES = (
        ('student', 'دانشجو'), 
        ('mentor', 'منتور'), 
        ('teacher', 'استاد')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices= ROLE_CHOICES)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            abstract = True
            ordering = ['-joined_at']

    def __str__(self):
            return f'{self.user.phone} - {self.role}'
       
class BaseCourseRegistration(models.Model):
    """
    Abstract base model for course registration requests.

    Used when a user applies for a course before joining.

    Fields:
    - full_name, phone, email: Contact information
    - role: Requested role in the course
    - status: Review status of the request
    - created_at: Submission time
    """

    STATUS_CHOICES = (
        ('pending', 'بررسی نشده'),
        ('reviewing', 'در حال بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'تایید نشده'),
    )

    ROLE_CHOICES = (
        ('student', 'دانشجو'),
        ('mentor', 'منتور'),
        ('teacher', 'استاد'),
    )

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']