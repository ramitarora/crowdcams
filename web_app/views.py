from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'title': 'Community Cams'}
    return render(request, 'index.html', context)

def protect_your_neighborhood(request):
	context = {'title': 'Protect your Neighborhood'}
	return render(request, 'protectyourneighborhood.html')

def how_it_works(request):
	context = {'title': 'How It Works'}
	return render(request, 'howitworks.html')
	
def project_founders(request):
	context = {'title': 'Project Founders'}
	return render(request, 'projectfounders.html')

def our_vision(request):
	context = {'title': 'Our Vision'}
	return render(request, 'ourvision.html')