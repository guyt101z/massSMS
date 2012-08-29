from massSMS.userupload.models import *
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

def send_SMS(modeladmin, request, queryset):
    selected = reduce(lambda x, y: str(x)+","+str(y), [user.pk for user in queryset])
    return HttpResponseRedirect("/admin/sendsms/%s" % selected)
send_SMS.short_description = "Send SMS to selected users"

def send_premade(modeladmin, request, queryset):
    selected = reduce(lambda x, y: str(x)+","+str(y), [msg.pk for msg in queryset])
    return HttpResponseRedirect("/admin/sendpremade/%s" % selected)
send_premade.short_description = "Send premade message with pre-defined recipients"

class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'group', 'school', 'cell_number', 'carrier')
    list_filter = ['school', 'group']
    actions = [send_SMS]

class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    list_display = ('name', 'recipient_str')
    actions = [send_premade]

admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)
