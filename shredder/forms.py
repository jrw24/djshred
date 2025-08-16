from django import forms
from .models import tuningInput, shredderInput 

class tuningInputForm(forms.ModelForm):
	class Meta:
		model = tuningInput
		fields = (
			'tuning',
			)
		widgets = {
			'tuning': forms.TextInput(attrs={'class': 'form-control'}),

		}
class shredderInputForm_alt(forms.Form):
	## testing without modelform
	accidentals = forms.CharField(max_length=128)
	key = forms.CharField(max_length=128)
	scale = forms.CharField(max_length=128)
	tuning = forms.CharField(max_length=128)


class shredderInputForm(forms.ModelForm):
	class Meta:
		model = shredderInput
		fields = (
			'accidentals', 'key', 'scale', 'tuning'
			)
		widgets = {
			'accidentals': forms.TextInput(attrs={'class': 'form-control'}),
			'key': forms.TextInput(attrs={'class': 'form-control'}),
			'scale': forms.TextInput(attrs={'class': 'form-control'}),
			'tuning': forms.TextInput(attrs={'class': 'form-control'})
		}