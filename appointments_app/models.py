from __future__ import unicode_literals
from django.db import models
from django.utils import timezone   

class AppointmentsData(models.Model):
	apmt_datetime =  models.DateTimeField(default=timezone.now)
	description = models.CharField(max_length=250,null=False)
