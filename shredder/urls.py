from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name='index'),
	path("notes_simple/", views.notes_simple, name='notes_simple'),
	path("tuned/", views.tuned, name='tuned'),
	path("custom_scale", views.custom_scale, name='custom_scale'),

]