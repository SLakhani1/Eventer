from django.db import models

class Events(models.Model):
	eventId = models.CharField(max_length=1000,primary_key=True)
	summary = models.CharField(max_length=200,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	createdBy = models.CharField(max_length=200,null=True,blank=True)
	organizedBy = models.CharField(max_length=200,null=True,blank=True)
	startDate = models.DateField(null=True,blank=True)
	startTime = models.TimeField(null=True,blank=True)
	endDate = models.DateField(null=True,blank=True)
	endTime = models.TimeField(null=True,blank=True)
	location = models.CharField(max_length=400,null=True,blank=True)
	hangoutLink = models.CharField(max_length=1000,null=True,blank=True)
	attachmentLink = models.CharField(max_length=1000,null=True,blank=True)

	def __str__(self):
		return str(self.summary) + " - " + str(self.startDate) + " - " + str(self.startTime)


class Attendees(models.Model):
	event = models.ForeignKey(Events, on_delete=models.CASCADE)
	displayName = models.CharField(max_length=200,null=True,blank=True)
	emailId = models.CharField(max_length=200,null=True,blank=True)
	responseStatus = models.BooleanField(default=False)

class Reminders(models.Model):
	event = models.ForeignKey(Events, on_delete=models.CASCADE)
	method = models.CharField(max_length=200,null=True,blank=True)
	minutes = models.IntegerField(null=True,blank=True)

class AuthTokens(models.Model):
	email = models.CharField(primary_key=True, max_length=200)
	token = models.JSONField()
