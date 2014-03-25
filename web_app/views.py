from django.shortcuts import render
import web_app.controllers.model_entry as model_entry
# Create your views here.
from web_app.models import UstreamListing


def home(request):
    streams = UstreamListing.objects.all()
    for stream in streams:
        stream.ustream_uid = str(stream.ustream_uid)

    context = {
        'title': 'Community Cams',
        'streams': streams
    }
    return render(request, 'index.html', context)


def protect_your_neighborhood(request):
    context = {'title': 'Protect your Neighborhood'}
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


def new_post(request):
    try:
        ustream_url = request.POST['ustream_url']
        emergency_contact = request.POST['emergency_contact']
        location_description = request.POST['location_description']
    except(KeyError):
        context = {'title':'Data not present'}
        return render(request, 'protectyourneighborhood.html', context)
    else:
        entry = model_entry.DataEntryHelper()
        entry.save_stream_details_to_model(ustream_url,emergency_contact,location_description)
        #return HttpResponseRedirect(reverse('', args=()))
        context = {'title':'Data stored successfully'}
        return render(request, 'protectyourneighborhood.html', context)