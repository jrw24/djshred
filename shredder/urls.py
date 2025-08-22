from django.urls import path
from . import views

urlpatterns = [
	# path("", views.accidentals, name='accidentals'),
	path("", views.index, name='index'),
	# path("notes/", views.notes, name='notes'),
	path("notes_simple/", views.notes_simple, name='notes_simple'),
	# path("shredder_input/", views.shredder_input, name='shredder_input'),
	# path("run_shredder/", views.run_shredder, name="run_shredder"),
	# path("image/", views.image, name="image"),

	# path("accidentals/", views.accidentals, name='accidentals'),
	# path("create-form/", views.create_tuning, name="create-tuning"),

]