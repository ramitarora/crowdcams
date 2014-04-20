from django.shortcuts import render
import web_app.controllers.model_entry as model_entry
from web_app.models import UstreamListing
from captcha.fields import ReCaptchaField
from django import forms
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    streams = UstreamListing.objects.all()
    streams = sorted(streams, key=lambda x:x.title)
    context = {
        'title': 'Crowdcams',
        'streams': streams[0:6]
    }
    return render(request, 'index.html', context)

def list(request):
    streams = UstreamListing.objects.all()
    streams = sorted(streams, key=lambda x:x.title)
    sections = {}
    for stream in streams:
        char = stream.title[0]
        if char not in sections:
            sections[char] = [stream]
        else:
            sections[char].append(stream)

    context = {
        'title': 'List of available Streams',
        'sections': sections
    }
    return render(request, 'listing.html', context)

def protect_your_neighborhood(request):
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
    form = SubmitForm()
    context = {'title': 'Protect your Neighborhood','form':form}
    return render(request, 'protectyourneighborhood.html', context)


def how_it_works(request):
    context = {'title': 'How It Works'}
    return render(request, 'howitworks.html', context)


def project_founders(request):
    context = {'title': 'Project Founders'}
    return render(request, 'projectfounders.html', context)


def our_vision(request):
    context = {'title': 'Our Vision'}
    return render(request, 'ourvision.html', context)


class SubmitForm(forms.Form):
    ustream_url = forms.CharField()
    emergency_contact = forms.IntegerField()
    location_description = forms.CharField()
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})


def new_post(request):
    if request.method == 'POST':
            form = SubmitForm(request.POST)
            if form.is_valid():
                ustream_url = form.cleaned_data['ustream_url']
                emergency_contact = form.cleaned_data['emergency_contact']
                location_description = request.POST['location_description']
                entry = model_entry.DataEntryHelper()
                entry.save_stream_details_to_model(ustream_url,emergency_contact,location_description)
                context = {'title':'Success','feedback_to_user':"Hurray!! Your video stream has been successfully added!"}
                return render(request, 'protectyourneighborhood.html', context)
            #processing the data
    else:
        form = SubmitForm()
    return render(request, 'protectyourneighborhood.html', {'form':form,})


def login(request):
    return HttpResponseRedirect('/')


def register(request):
    return HttpResponseRedirect('/')