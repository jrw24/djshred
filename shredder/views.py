from django.shortcuts import render
from django.http import HttpResponse
from .forms import tuningInputForm, shredderInputForm
from .models import Accidentals, Notes, Scales, Tunings, tuningInput, shredderInput

def index(request):
	# return HttpResponse("Get ready to shred!")
	context = {'form': tuningInputForm()}
	return render(request, 'index.html', context)

def create_tuning(request):
	if request.method == 'POST':
		pass
	return render(request, 'partials/form.html', {'form':tuningInputForm()})

def run_shredder(request):
	# print('test a shredder run')
	if request.method == 'POST':
	# if 'shredder_run' in request.POST:
		print('found shredder POST')
		form =  shredderInputForm(request.POST or None)
		if form.is_valid():
			# print(form)
			shredder_run = form.save()
			# print(shredder_run)

			# obj = shredderInput()
			# ob
			context = {'shredder_run' : shredder_run}
			return render(request, 'partials/run_shredder.html', context)

# Create your views here.
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
	accidentals = request.GET.get('accidentals')
	notes = Notes.objects.filter(accidentals=accidentals)
	context = {'notes': notes}
	return render(request, 'partials/notes.html', context)


def get_tuning(request):
	#
	context = {'form': tuningInputForm()}
	return render(request, 'index.html', context)