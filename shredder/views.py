from django.shortcuts import render
from django.http import HttpResponse
from .models import Accidentals, Notes, Scales

def index(request):
	return HttpResponse("Get ready to shred!")

# Create your views here.
def accidentals(request):
	accidentals = Accidentals.objects.all()
	scales = Scales.objects.all()
	context = {
		'accidentals': accidentals,
		'scales': scales}
	return render(request, 'set_accidentals.html', context)

def notes(request):
	accidentals = request.GET.get('accidentals')
	notes = Notes.objects.filter(accidentals=accidentals)
	context = {'notes': notes}
	return render(request, 'partials/notes.html', context)


def print_out_user_input(data):
	#
	return f"User input entered as {data}"