import os
import re
from django import forms
from django.db import models
from django.core.exceptions import ValidationError

def validate_phone(val):
    try:
        int(val)
    except ValueError:
        raise ValidationError("Input a valid 10-digit number (ex. 5401231234")
    if len(val) != 10:
        raise ValidationError("Input a valid 10-digit number (ex. 5401231234")

class User(models.Model):
        CARRIER_GATEWAY = {
           "Teleflip":"teleflip.com",
           "Alltel":"message.alltel.com",
           "Ameritech":"paging.acswireless.com",
           "Bellsouth":"bellsouth.cl",
           "CellularOne":"mobile.celloneusa.com",
           "Cingular":"mobile.mycingular.com",
           "Edge Wireless":"sms.edgewireless.com",
           "Metro PCS":"mymetropcs.com",
           "O2":"mobile.celloneusa.com",
           "Orange":"mobile.celloneusa.com",
           "Qwest":"qwestmp.com",
           "Rogers Wireless":"pcs.rogers.com",
           "Telus Mobility":"msg.telus.com",
           "US Cellular":"email.uscc.net",
           "Kajeet":"mobile.kajeet.net",
           "Element Mobile":"SMS.elementmobile.net",
           "Google Voice":"txt.voice.google.com",
           "Bluegrass Cellular":"sms.bluecell.com",
           "GoPhone":"cingulartext.com",
           "Cricket":"sms.mycricket.com",
           "Straight Talk":"vtext.com",
           "Simple Mobile":"smtext.com",
           "South Central Communications":"rinasms.com",
           "Qwest Wireless":"qwestmp.com",
           "Unicel":"utext.com",
           "TracFone":"txt.att.net",
           "Centennial Wireless":"cwemail.com",
           "Virgin Mobile":"vmobl.com",
           "Sprint PCS":"messaging.sprintpcs.com",
           "T-Mobile":"tmomail.net",
           "Nextel":"messaging.nextel.com",
           "Boost":"myboostmobile.com",
           "Verizon":"vtext.com",
           "ATT Wireless":"txt.att.net"
            }
        SCHOOL_CHOICES = (
            ("CO", "Central Office"),
            ("LCHS", "High School"),
            ("LCMS", "Middle School"),
            ("MNES", "Moss-Nuchols"),
            ("TJES", "Thomas Jefferson"),
            ("TES", "Trevillians"),
            ("JES", "Jouett"))
        CARRIER_CHOICES = [(carrier, carrier) for carrier in CARRIER_GATEWAY.keys()]
        GROUP_CHOICES = (
            ("Admin", "Administrator"),
            ("Teacher", "Teacher"),
            ("Staff", "Staff"))
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
        group = models.CharField(max_length=15, choices=GROUP_CHOICES)
	school = models.CharField(max_length=15, choices=SCHOOL_CHOICES)
        cell_number = models.CharField(max_length=10, validators=[validate_phone], unique=True, help_text="Example: 5409679999")
	carrier = models.CharField(max_length=35, choices=CARRIER_CHOICES, help_text="Hint: click on the dropdown and type the first letter of your carrier until it is selected.")

	def __unicode__(self):
	    return self.first_name+self.last_name+"@"+self.cell_number

        def cell_email(self):
            CARRIER_GATEWAY = {
               "Teleflip":"teleflip.com",
               "Alltel":"message.alltel.com",
               "Ameritech":"paging.acswireless.com",
               "ATT Wireless":"txt.att.net",
               "Bellsouth":"bellsouth.cl",
               "Boost":"myboostmobile.com",
               "CellularOne":"mobile.celloneusa.com",
               "Cingular":"mobile.mycingular.com",
               "Edge Wireless":"sms.edgewireless.com",
               "Sprint PCS":"messaging.sprintpcs.com",
               "T-Mobile":"tmomail.net",
               "Metro PCS":"mymetropcs.com",
               "Nextel":"messaging.nextel.com",
               "O2":"mobile.celloneusa.com",
               "Orange":"mobile.celloneusa.com",
               "Qwest":"qwestmp.com",
               "Rogers Wireless":"pcs.rogers.com",
               "Telus Mobility":"msg.telus.com",
               "US Cellular":"email.uscc.net",
               "Verizon":"vtext.com",
               "Virgin Mobile":"vmobl.com",
               "Kajeet":"mobile.kajeet.net",
               "Element Mobile":"SMS.elementmobile.net",
               "Google Voice":"txt.voice.google.com",
               "Bluegrass Cellular":"sms.bluecell.com",
               "GoPhone":"cingulartext.com",
               "Cricket":"sms.mycricket.com",
               "Straight Talk":"vtext.com",
               "Simple Mobile":"smtext.com",
               "South Central Communications":"rinasms.com",
               "Qwest Wireless":"qwestmp.com",
               "Unicel":"utext.com",
               "TracFone":"txt.att.net",
               "Centennial Wireless":"cwemail.com"
                }
            return self.cell_number+"@"+CARRIER_GATEWAY[self.carrier]

class UserForm(forms.ModelForm):

    class Meta:
        model = User

    cell_number = forms.CharField(max_length=10)


class Message(models.Model):
    name = models.CharField(max_length=35, help_text="A title for the message, used for admin purposes.")
    body = models.TextField()
    recipients = models.ManyToManyField(User)
    recipient_str = models.CharField(max_length=50, help_text="A short description of the recipient to whom this message is sent (ex: admins, teachers, etc.)")

    def __unicode__(self):
        return self.name

class MessageForm(forms.ModelForm):
    body = forms.CharField(max_length=140, widget=forms.Textarea)
    
    class Meta:
        model = Message
