from django.contrib import admin
from .models import Events, Attendees, Reminders, AuthTokens
# Register your models here.

admin.site.register(Events)
admin.site.register(Attendees)
admin.site.register(Reminders)
admin.site.register(AuthTokens)