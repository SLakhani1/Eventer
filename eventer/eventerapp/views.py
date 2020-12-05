from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from httplib2 import Http
from oauth2client import file, client, tools
from .models import Events, Attendees, Reminders, AuthTokens
import datetime
import requests
import pickle
import os

SCOPES = "https://www.googleapis.com/auth/calendar"

def login_page(request):
	user = request.user
	if user and user.is_authenticated:
		return redirect("/dashboard")
	return render(request,'eventerapp/src/views/Customers.vue',context=None)

def logout_view(request):
	if request.user:
		logout(request)
	return redirect("/")

def runservice():
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	
	if not creds or not creds.valid:
		flow = InstalledAppFlow.from_client_secrets_file('eventer/eventerapp/credentials.json', SCOPES)
		
		creds = flow.run_local_server(port=7058)
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)
	service = build('calendar', 'v3', credentials=creds)
	return service


def dashboard_view(request):
	if request.user.is_authenticated:
		eventId = summary = description = createdBy = organizedBy = startDate = startTime = endDate = endTime = location = hangoutLink = attachmentLink = None
		now = datetime.datetime.utcnow().isoformat() + 'Z'	
		service = runservice()
		eventsResult = service.events().list(
			calendarId='primary', singleEvents=True,	#, timeMin=now
			orderBy='startTime').execute()
		events = eventsResult.get('items', [])
		if not events:
			print('No upcoming events found.')
		for event in events:
			eventId = event['id']
			if Events.objects.filter(eventId=eventId):
				continue
			summary = event['summary']
			try:
				description = event['description']
			except:
				pass
			createdBy = event['creator']['email']
			organizedBy = event['organizer']['email']
			try:
				startDate = datetime.datetime.strptime(event['start']['dateTime'].split("+")[0],"%Y-%m-%dT%H:%M:%S").date()
			except:
				pass
			try:
				startTime = datetime.datetime.strptime(event['start']['dateTime'].split("+")[0],"%Y-%m-%dT%H:%M:%S").time()
			except:
				pass
			try:
				endDate = datetime.datetime.strptime(event['end']['dateTime'].split("+")[0],"%Y-%m-%dT%H:%M:%S").date()
			except:
				pass
			try:
				endTime = datetime.datetime.strptime(event['start']['dateTime'].split("+")[0],"%Y-%m-%dT%H:%M:%S").time()
			except:
				pass
			try:
				location = event['location']
			except:
				pass
			try:
				hangoutLink = event['hangoutLink']
			except:
				pass
			try:
				attachmentLink = event['attachment']['fileUrl']
			except:
				pass

			eventObject = Events.objects.create(
				eventId = eventId,
				summary = summary,
				description = description, 
				createdBy = createdBy,
				organizedBy = organizedBy,
				startDate = startDate,
				startTime = startTime,
				endDate = endDate,
				endTime = endTime,
				location = location,
				hangoutLink = hangoutLink,
				attachmentLink = attachmentLink
			)
			try:
				attendees = event['attendees']
				for attendee in attendees:
					displayName = attendee['displayName']
					emailId = attendee['email']
					responseStatus = attendee['responseStatus']
					if responseStatus == 'accepted':
						responseStatus = True
					else:
						responseStatus = False
					Attendees.objects.create(
						event = eventObject,
						displayName = displayName,
						emailId = emailId,
						responseStatus = responseStatus
					)
			except:
				pass
			try:
				reminders = event['reminders']['overrides']
				for reminder in reminders:
					method = reminder['method']
					minutes = reminder['minutes']
					Reminders.objects.create(
						event = eventObject,
						method = method,
						minutes = minutes
					)
			except:
				pass
		return render(request, 'dashboard.html',context={'events':events})
	else:
			return redirect("/")
