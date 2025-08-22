from django import forms
from .models import shredderInput 

class shredderInputForm(forms.ModelForm):
	class Meta:
		model = shredderInput
		fields = (
			'accidentals_defaults', 'key', 'scale', 'tuning', 'mode'
			)
		widgets = {
			'accidentals_defaults': forms.TextInput(attrs={'class': 'form-select'}),
			'key': forms.TextInput(attrs={'class': 'form-select'}),
			'scale': forms.TextInput(attrs={'class': 'form-select'}),
			'tuning': forms.TextInput(attrs={'class': 'form-select'}),
			'mode': forms.TextInput(attrs={'class': 'form-select'})
		}