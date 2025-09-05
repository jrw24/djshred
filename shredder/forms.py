from django import forms
from .models import shredderInput 

class shredderInputForm(forms.ModelForm):
	class Meta:
		model = shredderInput
		fields = (
			'accidentals_defaults', 
			'key', 
			'scale', 
			'tuning', 
			'tuned', 
			'mode',
			'scale_name',
			'scale_intervals',
			'screenWidth',
			'screenHeight'
			)
		widgets = {
			'accidentals_defaults': forms.TextInput(attrs={'class': 'form-select'}),
			'key': forms.TextInput(attrs={'class': 'form-select'}),
			'scale': forms.TextInput(attrs={'class': 'form-select'}),
			'tuning': forms.TextInput(attrs={'class': 'form-select'}),
			'tuned': forms.TextInput(attrs={'class': 'form-control'}),
			'mode': forms.TextInput(attrs={'class': 'form-select'}),
			'scale_name': forms.TextInput(attrs={'class': 'form-control'}),
			'scale_intervals': forms.TextInput(attrs={'class': 'form-control'}),
		}