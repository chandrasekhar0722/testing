from django.shortcuts import render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from csvtask.models import Company,Companydetail
import json
from django.utils import simplejson

def getdatabetweentwodate(request,c=None,day=None,month=None,year=None,d=None,m=None,y=None):
	companyname = '%s' % (c)
	startdate = '%s-%s-%s' % (day, month, year)
	print startdate
	enddate = '%s-%s-%s' % (d, m, y)
	print enddate
	
