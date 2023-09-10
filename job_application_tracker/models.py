from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class JobApplication(models.Model):
    class Meta:
        db_table = "JobApplication"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField(blank=True)
    expected_salary = models.IntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse("jobs:application", kwargs={"pk": self.id})
