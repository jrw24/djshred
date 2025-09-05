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
		# print('screenWidth', screenWidth)
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
			html_frag, scale_info = shredder.main(
				scale = shredder_run['scale'],
				key = shredder_run['key'],
				tuning= shredder_run['tuned'],
				flats = shredder_run['flats'],
				mode = shredder_run['mode'],
				django = '1',
				fretnumber = '24',
				scale_name = shredder_run['scale_name'],
				scale_intervals = shredder_run['scale_intervals'],
				screenWidth = shredder_run['screenWidth'],
				screenHeight = shredder_run['screenHeight'] )

			### add css style to html figure output
			html_fig = f'''
				<style type="text/css">
					#shredderfig {{
					width: 100%;
					height: auto;
					}}
				div#shredderfig {{ text-align: center}}
				</style>

				{html_frag}
				'''

			context['figure'] = html_fig
			context['scale_notes'] = scale_info[0]
			context['scale_degrees'] = scale_info[1]
			context['scale_ints'] = scale_info[2]
			context['scale_notes_string'] = ', '.join(scale_info[0])
			context['scale_degrees_string'] = ', '.join(scale_info[1])
			context['scale_ints_string'] = ', '.join(scale_info[2])
			# print(html_fig)
		else:
			print('ERRORS FOUND !!!')
			print(form.errors)
			## create new partial to handle completeion of form 
	else: ## plot empty fretboard
		pass
		# html_frag = shredder.plot_empty_fretboard()
		# html_fig = f'''
		# 	<style type="text/css">
		# 		#emptyfretboard {{
		# 		width: 100%;
		# 		height: auto;
		# 		}}
		# 	div#shredderfig {{ text-align: center}}
		# 	</style>

		# 	{html_frag}
		# 	'''

		# context['figure'] = html_fig

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

def tuned(request):
	tuned = request.GET.get('tuning')
	current_tune = request.GET.get('current_tune')
	context = {'tuned': tuned}
	if current_tune is not None:
		context['current_tune'] = current_tune
	return render(request, 'partials/tuned.html', context)


def custom_scale(request):
	scale_entry = request.GET.get('scale')
	scale_name = request.GET.get('scale_name')
	scale_intervals = request.GET.get('scale_intervals')

	context = {'scale_entry': scale_entry}
	if scale_name is not None:
		context['scale_name'] = scale_name
	if scale_intervals is not None:
		mod_scale_intervals = scale_intervals.replace(' ','')
		context['scale_intervals'] = mod_scale_intervals

	return render(request, 'partials/custom_scale.html', context)
