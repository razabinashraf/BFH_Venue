import events
from django.shortcuts import render,redirect
from .models import event
from django.shortcuts import get_object_or_404
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











    