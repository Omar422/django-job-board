from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

"""
# Django Model Fields Provide:
    - html widget
    - validation
    - db size
"""
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) # use single qutue because model after used

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name