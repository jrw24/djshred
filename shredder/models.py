from django.db import models

# Create your models here.
class Accidentals(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Notes(models.Model):
	name = models.CharField(max_length=128)
	accidentals = models.ForeignKey(
		Accidentals, 
		on_delete=models.CASCADE,
		# on_delete=models.PROTECT, 
		related_name='accidentals')

	def __str__(self):
		return self.name

class Scales(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Tunings(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Modes(models.Model):
	name = models.CharField(max_length=24)

	def __str__(self):
		return self.name

class shredderInput(models.Model):
	accidentals_defaults = models.CharField(max_length=128)
	key = models.CharField(max_length=128)
	scale = models.CharField(max_length=128)
	tuning = models.CharField(max_length=128, default='EADGBE')
	tuned = models.CharField(max_length=128)
	mode = models.CharField(max_length=24, default='note')
	scale_name = models.CharField(max_length=128, blank=True)
	scale_intervals = models.CharField(max_length=128, blank=True)
	screenWidth = models.CharField(max_length=24)
	screenHeight = models.CharField(max_length=24)

	def __str__(self):
		return f'{self.key}_{self.scale}_{self.tuning}'