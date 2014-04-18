from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def form(request):
	return render(request,"feedback/home.html")

def register(request):
	from feedback.models import query
	name = request.POST['name']
	email = request.POST['email']
	phone = request.POST['phone']
	service = request.POST['service'] 
	budget = request.POST['budget']
	loc = request.POST['location']
	date = request.POST['date']

	detail = query(Name=name,Email=email,Phone=phone,
		Serivce=service,Location=loc,Budget=budget,
		Date=date)

	detail.save()

	return HttpResponseRedirect('/feedback/')
