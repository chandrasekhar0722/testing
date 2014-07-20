from django.db import models
from django.conf import settings

import datetime


class Company(models.Model):
	code = models.AutoField(primary_key=True)
	companyname = models.CharField(max_length=50)
	sc_group = models.CharField(max_length=250)
	sc_type = models.CharField(max_length=250)
	class Meta:
        	db_table = u'company'

class Companydetail(models.Model):
    	sc_name = models.IntegerField()
    	opening = models.CharField(max_length=750)
    	high = models.CharField(max_length=750)
    	low = models.CharField(max_length=750)
    	close = models.CharField(max_length=750)
    	last = models.CharField(max_length=750)
    	prevclose = models.CharField(max_length=750)
    	no_trades = models.CharField(max_length=750)
    	no_of_shirs = models.CharField(max_length=750)
    	net_turnov = models.CharField(max_length=750)
    	date = models.CharField(max_length=750)
    	#date = models.DateField(settings.DATE_INPUT_FORMATS)
    	class Meta:
        	db_table = u'companydetail'