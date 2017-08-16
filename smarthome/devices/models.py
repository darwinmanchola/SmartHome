from __future__ import unicode_literals

from django.db import models


class Device(models.Model):
	location=models.CharField(max_length=100)
	gpio=models.IntegerField()
	state=models.BooleanField(default=False)

	def __str__(self):
		return self.location