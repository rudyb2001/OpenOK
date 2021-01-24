from django.db import models
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    # Mapping your own personal variables to database storage
    # ProductID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120, blank=True, null=False)
    # max_length = required
    # blank = whether or not field is required to be filled out
    # null = whether or not field can be empty in the database
    description = models.TextField(blank=True, null=True)
    #price = models.DecimalField(max_digits=100, decimal_places=2)
    #summary = models.TextField()
    resources = models.TextField(blank=True, null=True)
    # How to update values of current product objects
    #boo = models.BooleanField() # null=True, default=True
    #password = models.CharField(max_length=12, blank=False, null=False, default="pass")

    def get_absolute_url(self):
        return "/courses/{0}/".format(self.id)
        #reverse("course-detail", kwargs = {"id": self.id})