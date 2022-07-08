from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomInfo
from .models import TransacInfo

def custominfo(request):
	return render(request, 'model1_custominfo.html')
	if request.method == "POST":
		CustomInfo.objects.create(uname=request.POST['name'],
			firstname=request.POST['FirstName'],
			lastname=request.POST['LastName'],
			contactnumber=request.POST['ContactNumber'],
			email=request.POST['Email'],
			)
		return redirect('/')
	CustomInfoPoll = CustomInfo.objects.all()
	return render(request, 'model1_custominfo.html',{'input_IngameInfo': CustomInfoPoll})

def ordertransac(request):
	return render(request, 'model2_order.html',)
	

