from django.contrib import admin
from .models import event,register_event
# Register your models here.
admin.site.register(event)
admin.site.register(register_event)