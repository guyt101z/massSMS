from django.shortcuts import render_to_response
from models import User, UserForm
from django.http import HttpResponse
from django.template import RequestContext
from django.core.mail import EmailMessage

def home(request, *args, **kwargs):
    # input view
    if request.method == "GET":
        form = UserForm()
    # form processing
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            notification = EmailMessage("New LCPS SMS-Send User",
                    user.first_name+" "+user.last_name+" ("+user.school+") has registered for the service.",
                    "test@example.com", ["recto.ralph@gmail.com"])
            notification.send()
            return HttpResponse("Thank you!")
    return render_to_response("home.html", {"form": form}, context_instance=RequestContext(request))
