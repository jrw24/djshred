from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore
from .forms import shredderInputForm
from .models import Accidentals, Notes, Scales, Tunings, shredderInput, Modes
from matplotlib import pyplot as plt
import mpld3
from shredderscales import shredder

def index(request):
	# return HttpResponse("Get ready to shred!")
	
	accidentals_defaults = Accidentals.objects.all()
	scales_defaults = Scales.objects.all()
	tunings_defaults = Tunings.objects.all()
	modes_defaults = Modes.objects.all()
	accidentals = accidentals_defaults

	context = {
		'accidentals_defaults': accidentals_defaults,
		'scales_defaults': scales_defaults,
		'tunings_defaults': tunings_defaults,
		'accidentals' : accidentals,
		'modes_defaults' : modes_defaults
		}

	if request.method == 'POST':
		form =  shredderInputForm(request.POST or None)
		if form.is_valid():
			shredder_run = form.cleaned_data
			
			## define sharps or flats:
			if shredder_run['accidentals_defaults'] == '1':
				shredder_run['flats'] = 'sharps'
			elif shredder_run['accidentals_defaults'] == '2':
				shredder_run['flats'] = 'flats'
			else:
				shredder_run['flats'] = 'auto'
			context['shredder_run'] = shredder_run	

			### shredder plotting 
			html_fig = shredder.main(
				scale = shredder_run['scale'],
				key = shredder_run['key'],
				tuning= shredder_run['tuning'],
				flats = shredder_run['flats'],
				mode = shredder_run['mode'],
				django = '1',
				fretnumber = '24')

			context['figure'] = html_fig

		else:
			print('ERRORS FOUND !!!')
			print(form.errors)
			## create new partial to handle completeion of form 
	return render(request, 'index.html', context)

def notes_simple(request):
	accidentals_defaults = request.GET.get('accidentals_defaults')
	key_test = request.GET.get('key')
	notes_defaults = Notes.objects.filter(accidentals=accidentals_defaults)
	context = {'notes_defaults': notes_defaults}
	shredder_run = request.GET.get('shredder_run')
	if key_test is not None:
		context['current_key'] = key_test
	return render(request, 'partials/notes_simple.html', context)

