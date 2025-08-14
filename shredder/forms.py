from django import forms
from .models import shredderInput 

class shredderInputForm(forms.Form):
	class Meta:
		model = shredderInput
		fields = (
			'name', 'accidentals', 'key', 'tuning', 'scale'
			)
		widgets = {
			

		}