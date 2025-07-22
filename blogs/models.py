from django.db import models
from accounts.models import User




class CategoryBlog(models.Model):
    name = models.CharField(unique=True, max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Category name is {self.name}"
    





class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploaded_by = models.ForeignKey(to=User, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)


    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    blogcategory = models.ForeignKey(to=CategoryBlog, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to="articles/", null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


