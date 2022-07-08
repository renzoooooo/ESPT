from django.db import models

class CustomInfo(models.Model):
	firstname=models.CharField(blank = True)
	lastname=models.CharField(blank = True)
	contactnumber=models.IntegerField(blank = True)
	emailaddress=models.CharField(blank = True)

class TransacInfo(models.Model):
	game=models.CharField(blank = True)
	ticket=models.CharField(blank = True)
	quantity=models.CharField(blank = True)
	payment=models.CharField(blank = True)
	courier=models.CharField(blank = True)
	transactiondate=models.CharField(blank = True)
	deliverydate=models.CharField(blank = True)
	