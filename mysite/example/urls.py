from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	path(r'example_get/<str:var_a>/<int:var_b>',  views.example_get), #this is the name of a funciton#
	path(r'example_post/', views.example_post),
	path(r'fib/', views.fib), #this is the address to access the definition
	path(r'practice/', views.fib), #this is the address to access the definition
]