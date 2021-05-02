from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from contact_us.forms import ContactUsForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse()
        else:
            return HttpResponseBadRequest('OK')
    else:
        return HttpResponseBadRequest("400")
