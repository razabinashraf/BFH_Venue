import events
from django.shortcuts import render,redirect
from .models import event
from django.shortcuts import get_object_or_404
from .models import event,event_registration
from django.contrib import messages
# Create your views here.
def view_events(request) :
    events = event.objects.all()
    return render(request, 'view_events.html', {'events': events})

def create_event(request) :
    if request.method == 'POST' :
        title = request.POST['title']
        datetime = request.POST['datetime']
        location = request.POST['location']
        max_participants = request.POST['max_participants']
        description = request.POST['description']
        Event = event(title=title,datetime=datetime,location=location,max_participants=max_participants,description=description,user_id=request.user)
        Event.save()
        print('user created')
        return redirect('/events/view')
    else:
        return render(request, 'create_event.html',)

def profile(request, id):
    the_id = get_object_or_404(event, id=id)
    return render(request, 'profile.html', {'id': id,})    











    
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
