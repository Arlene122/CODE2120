from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

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

			




			# base_url variable to store url 
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			  
			# Give city name 
			city_name = input("Enter city name : ") 
			  
			# complete_url variable to store 
			# complete url address 
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
			  
			# get method of requests module 
			# return response object 
			response = requests.get(complete_url) 
			  
			# json method of response object  
			# convert json format data into 
			# python format data 
			x = response.json() 
			  
			# Now x contains list of nested dictionaries 
			# Check the value of "cod" key is equal to 
			# "404", means city is found otherwise, 
			# city is not found 
			if x["cod"] != "404": 
			  
			    # store the value of "main" 
			    # key in variable y 
			    y = x["main"] 
			  
			    # store the value corresponding 
			    # to the "temp" key of y 
			    current_temperature = y["temp"] 
			  
			  
			    # store the value of "weather" 
			    # key in variable z 
			    z = x["weather"] 
			  
			    # store the value corresponding  
			    # to the "description" key at  
			    # the 0th index of z 
			    weather_description = z[0]["description"] 
			  
			    # print following values 
			    return JsonResponse({"practice" +
			                    str(current_temperature) + 
			          "\n atmospheric pressure (in hPa unit) = " +

			          "\n description = " +
			                    str(weather_description)}) 
			  
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				other = sys.exc_info()[0].__name__
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				errorType = str(exc_type)
				return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
		else:
			return JsonResponse(jsob) #this is returning HTML


