from django.db import models

import datetime


class Company(models.Model):
	"""docstring for Company"""
	sc_code = models.IntegerField()
	companyname = models.CharField(max_length=50)
	


class Companydetail(models.Model):
	company = models.ForeignKey(Company)
	open = models.CharField(max_length=750)
	high = models.CharField(max_length=750)
	low = models.CharField(max_length=750)
	close = models.CharField(max_length=750)
	last = models.CharField(max_length=750)
	prevclose = models.CharField(max_length=750)
	no_trades = models.CharField(max_length=750)
	no_of_shirs = models.CharField(max_length=750)
	net_turnov = models.CharField(max_length=750)
	date = models.CharField(max_length=750)

"""class Company(models.Model):
	code = models.AutoField(primary_key=True)
	companyname = models.CharField(max_length=50)
	sc_group = models.CharField(max_length=250)
	sc_type = models.CharField(max_length=250)
	class Meta:
        	db_table = u'company'

class Companydetail(models.Model):
    	sc_name = models.IntegerField()
    	open = models.CharField(max_length=750)
    	high = models.CharField(max_length=750)
    	low = models.CharField(max_length=750)
    	close = models.CharField(max_length=750)
    	last = models.CharField(max_length=750)
    	prevclose = models.CharField(max_length=750)
    	no_trades = models.CharField(max_length=750)
    	no_of_shirs = models.CharField(max_length=750)
    	net_turnov = models.CharField(max_length=750)
    	date = models.CharField(max_length=750)
    	class Meta:
        	db_table = u'companydetail'"""
"""class CompanyDetail(models.Model):
	sc_name = models.ForeignKey(Company)
    	open = models.CharField(max_length=250)
    	high = models.CharField(max_length=250)
    	low = models.CharField(max_length=250)
    	close = models.CharField(max_length=250)
    	last  = models.CharField(max_length=250)
    	prevclose  = models.CharField(max_length=250)
    	no_trades = models.CharField(max_length=250)
    	no_of_shirs = models.CharField(max_length=250)
    	net_turnov = models.CharField(max_length=250)
        date = models.CharField(max_length=250)
	class Meta:
        	db_table = u'companydetail'"""
