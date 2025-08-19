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

class tuningInput(models.Model):
	name = models.CharField(default='EADGBE', max_length=128)
	tuning = models.CharField(max_length=128)

	def __str__(self):
		return self.name
		# return f'{self.key}_{self.scale}_{self.tuning}' 

class shredderInput(models.Model):
	accidentals_defaults = models.CharField(max_length=128)
	key = models.CharField(max_length=128)
	scale = models.CharField(max_length=128)
	tuning = models.CharField(max_length=128)

	def __str__(self):
		return f'{self.key}_{self.scale}_{self.tuning}'