from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore
from .forms import tuningInputForm, shredderInputForm
from .models import Accidentals, Notes, Scales, Tunings, tuningInput, shredderInput, Modes
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
	# print(accidentals_defaults)
	# print(accidentals)
	context = {
		'accidentals_defaults': accidentals_defaults,
		'scales_defaults': scales_defaults,
		'tunings_defaults': tunings_defaults,
		'accidentals' : accidentals,
		'modes_defaults' : modes_defaults
		}

	if request.method == 'POST':
	# if 'shredder_run' in request.POST:
		print('found shredder POST')
		# print('post context: ', context)

		form =  shredderInputForm(request.POST or None)
		# print(form)
		if form.is_valid():
			print(form.cleaned_data)
			shredder_run = form.cleaned_data
			## define sharps or flats:
			if shredder_run['accidentals_defaults'] == '1':
				shredder_run['flats'] = 'sharps'
			elif shredder_run['accidentals_defaults'] == '2':
				shredder_run['flats'] = 'flats'
			else:
				shredder_run['flats'] = 'auto'

			print(' --- shredder run dict ---')
			for s in shredder_run:
				print(s, shredder_run[s])

			print(' --- end shredder run dict ---')
			context['shredder_run'] = shredder_run	

			### plotting test

			# fig, ax = plt.subplots(figsize=(4,4))
			# x_values = [1, 2, 3, 4]
			# y_values = [2, 4, 1, 5]

			# ax.plot(x_values, y_values)
			# html_fig = mpld3.fig_to_html(fig)
			# context['figure'] = html_fig

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

			# print('accidentals run')
	print('final_context: ')
	for k,v in context.items():
		if k != 'figure':
			print(k, v)

	# print('*** loading plot! ***')
	# print('*** loading plot! ***')
	# print('*** loading plot! ***')


	# buffer = BytesIO()
	# fig, ax = plt.subplots(figsize=(4,4))

	# x_values = [1, 2, 3, 4]
	# y_values = [2, 4, 1, 5]
	# ax.plot(x_values, y_values)
	# plt.savefig(buffer, format="png")
	# buffer.seek(0)
	# image_png = buffer.getvalue()
	# buffer.close()

	# graphic = base64.b64encode(image_png)
	# graphic = graphic.decode('utf-8')
	# context['graphic'] = graphic


	return render(request, 'index.html', context)

# def shredder_input(request):
# 	if request.method == 'POST':
# 		print('post method found')
# 		form = shredderInputForm(request.POST)

# 		if form.is_valid():
# 			print(form.cleaned_data)
# 			data = form.cleaned_data
# 			context = {
# 				'accidentals': data['accidentals'],
# 				'key': data['key'],
# 				'scales': data['scale'],
# 				'tunings': data['tuning']
# 			}
# 			return(render, 'partials/run_shredder.html', context)
# 		else:
# 			print(form.errors)
# 			## create new partial to handle completeion of form 

def run_shredder(request):
	"""
	main view for running shredder after getting inputs
	"""
	# print('test a shredder run')
	if request.method == 'POST':
		pass
	# # if 'shredder_run' in request.POST:
	# 	print('found shredder POST')
	# 	form =  shredderInputForm(request.POST or None)
	# 	if form.is_valid():
	# 		print(form.cleaned_data)
	# 		shredder_run = form.cleaned_data
	# 		## define sharps or flats:
	# 		if shredder_run['accidentals_defaults'] == '1':
	# 			shredder_run['sharps'] = 'sharps'
	# 		elif shredder_run['accidentals_defaults'] == '2':
	# 			shredder_run['sharps'] = 'flats'
	# 		else:
	# 			print('sharps or flats not set!')

	# 		context = {
	# 			'shredder_run': shredder_run
	# 		}
	# 		print('^^ context ^^')
	# 		print(context)
	# 		# return(render, 'partials/run_shredder.html', context)
	# 		# return render(request, 'partials/run_shredder.html', context)
	# 		return render(request, 'index.html', context)

	# 	else:
	# 		print(form.errors)
	# 		## create new partial to handle completeion of form 

def create_tuning(request):
	if request.method == 'POST':
		pass
	return render(request, 'partials/form.html', {'form':tuningInputForm()})

def accidentals(request):
	"""
	main script for running the program at the moment
	"""
	if request.method == 'POST':
		form = shredderInputForm(request.POST)

		"""
		dir(form) when invalid

		"""



		if not form.is_valid():
			print('!! invalid form')
			print(dir(form))
			print('/n')
			print(form.cleaned_data) # {'accidentals': '2', 'tuning': '2'}
			print('tuning?', form.cleaned_data['tuning'])
			print(form.errors)
		if form.is_valid():
			print(form.cleaned_data)
			data = form.cleaned_data
			context = {
				'accidentals': data['accidentals'],
				'key': data['key'],
				'scales': data['scale'],
				'tunings': data['tuning']
			}
			## create new partial to handle completeion of form 


	else:

		accidentals = Accidentals.objects.all()
		scales = Scales.objects.all()
		tunings = Tunings.objects.all()
		context = {
			'accidentals': accidentals,
			'scales': scales,
			'tunings': tunings}
		# print('accidentals run')
	return render(request, 'set_accidentals.html', context)

def notes(request):
	print('-- starting notes request --')
	accidentals_defaults = request.GET.get('accidentals_defaults')
	print('accidentals_defaults:', accidentals_defaults)

	print('-- setting session store --')
	s = SessionStore()
	print(dir(s))
	print(s.keys())
	if 'shredder_run' in s:
		shredrun = s['shredder_run']
		print('shredrun', shredrun)

	notes_defaults = Notes.objects.filter(accidentals=accidentals_defaults)
	print('notes_defaults:', notes_defaults)
	context = {'notes_defaults': notes_defaults}
	shredder_run = request.GET.get('shredder_run')
	print('shredder_run', shredder_run)
	if shredder_run is not None:
		current_key = shredder_run['key']
		context['current_key'] = current_key
	print('notes context-> :', context)
	return render(request, 'partials/notes.html', context)

def notes_simple(request):
	print('-- starting notes simple request --')
	accidentals_defaults = request.GET.get('accidentals_defaults')
	print('accidentals_defaults:', accidentals_defaults)

	key_test = request.GET.get('key')
	print( ' ------------------ ')
	print(key_test, '<--- key test')
	print( ' ------------------ ')
	# print('-- setting session store --')
	# s = SessionStore()
	# print(dir(s))
	# print(s.keys())
	# if 'shredder_run' in s:
	# 	shredrun = s['shredder_run']
	# 	print('shredrun', shredrun)

	notes_defaults = Notes.objects.filter(accidentals=accidentals_defaults)
	print('notes_defaults:', notes_defaults)
	context = {'notes_defaults': notes_defaults}
	shredder_run = request.GET.get('shredder_run')
	print('shredder_run', shredder_run)
	if key_test is not None:
		context['current_key'] = key_test
	print('notes context-> :', context)
	return render(request, 'partials/notes_simple.html', context)

def get_tuning(request):
	#
	context = {'form': tuningInputForm()}
	return render(request, 'index.html', context)

def image(request):

	print('*** loading plot! ***')
	print('*** loading plot! ***')
	print('*** loading plot! ***')


	# buffer = BytesIO()
	# fig, ax = plt.subplots(figsize=(4,4))

	# x_values = [1, 2, 3, 4]
	# y_values = [2, 4, 1, 5]
	# ax.plot(x_values, y_values)
	# plt.savefig(buffer, format="png")
	# buffer.seek(0)
	# image_png = buffer.getvalue()
	# buffer.close()

	# graphic = base64.b64encode(image_png)
	# graphic = graphic.decode('utf-8')
	# context = {'graphic': graphic}

	fig, ax = plt.subplots(figsize=(4,4))
	x_values = [1, 2, 3, 4]
	y_values = [2, 4, 1, 5]

	ax.plot(x_values, y_values)
	html_fig = mpld3.fig_to_html(fig)
	context = {'figure': html_fig}

	return render(request, 'image.html', context)
