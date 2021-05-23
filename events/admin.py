from django.contrib import admin
from .models import event,event_registration
# Register your models here.
admin.site.register(event)
admin.site.register(event_registration)