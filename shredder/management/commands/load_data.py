from django.core.management.base import BaseCommand
from shredder.models import Accidentals, Notes, Scales, Tunings, Modes
from shredderscales.scales import Scales as sc

class Command(BaseCommand):
	help = 'Load Accidentals and Notes'

	def handle(self, *args, **kwargs):
		## remove stored Notes, Scales, and Tunings on loading
		Notes.objects.all().delete()
		Scales.objects.all().delete()
		Tunings.objects.all().delete()
		Modes.objects.all().delete()

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

		## load scales
		Scales.objects.create(name='*custom*')
		avail_scales = list(sc.available_scales.keys())
		for s in avail_scales:
			print(s)
			Scales.objects.create(name=s)

		## load tunings for now:
		tunings = [
			'EADGBE',
			'DADGBE',
			'CGCFAD',
			'D#G#C#F#A#D#',
			'EbAbDbGbBbEb',
			'BEADGBE',
			'GCGCFAD',
			'G#D#G#C#F#A#D#',
			'F#BEADGBE'
		]

		for tune in tunings:
			Tunings.objects.create(name=tune)

		
		## load modes:
		modes = [
			'note',
			'degree',
			'interval'
		]

		for m in modes:
			Modes.objects.create(name=m)
