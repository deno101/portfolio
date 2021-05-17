from django.forms import models
from contact_us.models import ContactUs


class ContactUsForm(models.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
