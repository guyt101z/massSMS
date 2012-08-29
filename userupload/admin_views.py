from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from models import User, Message

def sendpremade(request, ids):
    #Dialog for sending a premade message (action in Message model admin)

    msg_ids = [int(id) for id in ids.split(",")]
    messages = []
    for id in msg_ids:
        messages.append(Message.objects.get(pk=id))
    for msg in messages:
        m = EmailMessage("", msg.body, "hello@gmail.com", 
                [user.cell_email() for user in msg.recipients.all()],
                headers = {"From":"LCPS IT", "Sender":"Ralph J. Recto"})
        m.send()
    return render_to_response("admin/sendpremade-dialog.html", {"num_msgs":len(messages)}, context_instance=RequestContext(request))

def sendsms_dialog(request, ids):
    #Dialog for sending an SMS

    user_ids = [int(id) for id in ids.split(",")]
    users = []
    for id in user_ids:
        users.append(User.objects.get(pk=id))
    msgdict = {}
    return render_to_response("admin/sendsms-dialog.html", {"users":users, "msg_list":Message.objects.all()}, context_instance=RequestContext(request))

@csrf_protect
def sendsms_submit(request):
    #Sends message to users

    user_ids = [int(id) for id in request.POST["ids"].split(",")]
    users = []
    for id in user_ids:
        users.append(User.objects.get(pk=id))
    message = request.POST["message"]
    #contact footer to be added
    if request.POST["contact_flag"] == "on":
        message+= (" (contact %s)" % request.POST["cellcontact"])
    m = EmailMessage("", message, "hello@gmail.com", 
            [user.cell_email() for user in users],
            headers = {"From":"LCPS IT", "Sender":"Ralph J. Recto"})
    m.send()
    return render_to_response("admin/sendsms-submit.html", {"num_users":len(users)}, context_instance=RequestContext(request))

sendsms_dialog = staff_member_required(sendsms_dialog)
sendsms_submit = staff_member_required(sendsms_submit)

