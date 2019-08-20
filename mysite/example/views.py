from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys
import random

# Create your views here.

def example_get(request, var_a, var_b):#these variables must be the same name as in the function in the url file.  This is running a get request
	try:#Try - this prevents Django from breaking, and gives an object about the error and tells you about the error#
		returnob = {
		"data": "bubblegum %s < pizza %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt #this is a decorator -> These are put before a function
def example_post(request): #example_post -> This allows you to send data with the request
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			jsob = json.loads(data) #changes from this line are from Lecture 2 recording

			index = 0
			for i in jsob["demo"]:
				index += 1

			return JsonResponse({"count":index})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("ONLY POST REQUESTS") #this is returning HTML





@csrf_exempt #this is a decorator -> These are put before a function
def fib(request): #example_post -> This allows you to send data with the request
	jsob = {"StartNumber": 0, "Length": 10}
	log = [] #helps to print errors if there are problems
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received) #changes from this line are from Lecture 2 recording

			#######################################
			#EVERYTHING ABOVE THIS LINE IS REQURED#
			#######################################

			startnumber = int(jsob["StartNumber"]) #int makes sure that even if someone gives us a string it is now an integer
			length= int(jsob["Length"])
			loop = range(length) #this is making an array of numbers

			numarray = []
			fibno = startnumber #this is the current number
			addno = 2
			for l in loop:
				numarray.append(fibno)
				fibno = fibno + addno
				addno = fibno - addno

			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob) #this is returning HTML






@csrf_exempt #this is a decorator -> These are put before a function
def practice(request): #example_post -> This allows you to send data with the request
	jsob = {"Country name": 0, "Current Weather": 3}
	log = [] #helps to print errors if there are problems
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received) #changes from this line are from Lecture 2 recording

			#######################################
			#EVERYTHING ABOVE THIS LINE IS REQURED#
			#######################################

		NAMES = ['Adam', 'Betty', 'Charlie', 'Debbie', 'Elaine', 'Frank' 'George','Harry', 'Igor', 'Jack', 'Kevin', 'Larry', 'Moe', 'Nancy', 'Ophelia', 'Phil', 'Quentin']
		FRUIT = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

		sCounter = 0
		fCounter = 5


		while sCounter <= fCounter:
		    sCounter += 1 

			return JsonResponse ().format(random.choice(NAMES))
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse(jsob) #this is returning HTML

