from django.core.management.base import BaseCommand
from shredder.models import Accidentals, Notes, Scales
from shredderscales.scales import Scales as sc

class Command(BaseCommand):
	help = 'Load Accidentals and Notes'

	def handle(self, *args, **kwargs):
		Notes.objects.all().delete()
		accidentals_names = [
			'sharps', 'flats'
		]

		if not Accidentals.objects.count():
			for accidentals_name in accidentals_names:
				Accidentals.objects.create(name=accidentals_name)

		## sharps:
		sharps = Accidentals.objects.get(name='sharps')

		sharp_notes = [
			'A',
			'A#',
			'B',
			'C',
			'C#',
			'D',
			'D#',
			'E',
			'F',
			'F#',
			'G',
			'G#',
		]

		for note in sharp_notes:
			Notes.objects.create(name=note, accidentals=sharps)

		## flats:
		flats = Accidentals.objects.get(name='flats')

		flat_notes = [
			'A',
			'Bb',
			'B',
			'C',
			'Db',
			'D',
			'Eb',
			'E',
			'F',
			'Gb',
			'G',
			'Ab',
		]

		for note in flat_notes:
			Notes.objects.create(name=note, accidentals=flats)
		## when shredderscales is updated -- use this 250813
		# scales = list(sc.available_scales.keys())
		# print(scales)

		## for now:
		scales = [
			'chromatic',
			'major',
			'minor',
			'harmonic-minor',
			'pentatonic-major',
			'pentatonic-minor',
			'phrygian-major'
		]

		for scale in scales:
			Scales.objects.create(name=scale)

		

