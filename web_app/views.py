import json
from django.core.context_processors import csrf
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
import web_app.controllers.model_entry as model_entry
from web_app.models import UstreamListing
from captcha.fields import ReCaptchaField
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from web_app.tasks import face_detect


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


def view_stream(request):
    vid = request.GET['vid']
    stream = UstreamListing.objects.get(ustream_uid=vid)
    context = {
        'stream': stream
    }
    return render(request, "view_stream.html", context)


def app_regions(request):
    if request.method == "GET":
        vid = request.GET['vid']
        stream = UstreamListing.objects.get(ustream_uid=vid)
        context = {
            'stream': stream
        }
        return render(request, "app_regions.html", context)
    else:
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        width = int(request.POST.get('width'))
        height = int(request.POST.get('height'))
        stream_url = str(request.POST.get('stream_url'))
        name = str(request.POST.get('name'))
        face_detect.delay(x,y,width,height, stream_url)
        response = {'status': 'true'}
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')


def app_smiles(request):
    vid = request.GET['vid']
    stream = UstreamListing.objects.get(ustream_uid=vid)
    context = {
        'stream': stream
    }
    context.update(csrf(request))
    return render(request, "app_smiles.html", context)