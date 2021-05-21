import events
from django.shortcuts import render
from .models import event
from django.shortcuts import get_object_or_404
# Create your views here.
def view_events(request) :
    events = event.objects.all()
    print(events[0].location)
    return render(request, 'view_events.html', {'events': events})

def create_event(request) :
    events = event.objects.all()
    print(events[0].location)
    return render(request, 'view_events.html',)

def profile(request, id):
    the_id = get_object_or_404(event, id=id)
    return render(request, 'profile.html', {'id': id,})    