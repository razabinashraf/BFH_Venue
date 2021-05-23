import events
from django.shortcuts import render,redirect
from .models import event,event_registration
from django.contrib import messages
# Create your views here.
def view_events(request) :
    events = event.objects.all()
    return render(request, 'view_events.html', {'events': events})

def create_event(request) :
    return render(request, 'create_event.html',)

def register_event(request, event_id):
    if request.user.is_authenticated:
        event_obj = event.objects.get(pk=event_id)
        event_registration.objects.create(user=request.user, event=event_obj)
        messages.success(request, 'Succesfully registered for event')
        return redirect('/events/registrations')

def view_registrations(request) :
    registrations = event_registration.objects.all()
    return render(request, 'view_registrations.html', {'registrations':registrations })