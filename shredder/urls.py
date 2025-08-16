from django.urls import path
from . import views

urlpatterns = [
	path("", views.accidentals, name='accidentals'),
	path("run-shredder/", views.run_shredder, name="run-shredder"),
	path("index/", views.index, name='index'),
	path("create-form/", views.create_tuning, name="create-tuning"),
	path("notes/", views.notes, name='notes')
]