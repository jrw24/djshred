from django.urls import path
from . import views

urlpatterns = [
	path("", views.accidentals, name='accidentals'),
	path("notes/", views.notes, name='notes')
]