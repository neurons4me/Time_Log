from django.db import models

# Create your models here.
class Time_record(models.Model):
    user_id = models.CharField(max_length=30, null=True, blank=True)
    task_name = models.CharField(max_length=60, null=True, blank=True)
    project_name = models.CharField(max_length=60, null=True, blank=True)
    client_name = models.CharField(max_length=40, null=True, blank=True)
    activity_start = models.DateTimeField(null=True, blank=True)
    activity_end = models.DateTimeField(null=True, blank=True)
    clocked_in = models.BooleanField()


# time record changelog model should log: date of change, change type, user who made change, and record ID for all Time_record changes
