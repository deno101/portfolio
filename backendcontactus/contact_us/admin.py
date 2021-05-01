from django.contrib import admin
from contact_us.models import ContactUs


# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'message')
    list_display = ('name', 'email', 'message', 'date')


admin.site.register(ContactUs, ContactUsAdmin)
