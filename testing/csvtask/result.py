from django.shortcuts import render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from csvtask.models import Company,Companydetail
import json
from django.utils import simplejson


def getdata(request,companyname=None,day=None,month=None,year=None):
	companyname = '%s' % (companyname)
	date = '%s-%s-%s' % (day, month, year)
	a = Company.objects.filter(companyname=companyname).values()
	for i in a:
		b = list(Companydetail.objects.filter(date=date,sc_name=i['code']).values('open','close'))
	return HttpResponse(simplejson.dumps(b,indent=2), mimetype='application/json')


"""def getdatabetweentwodate(request,c=None,day=None,month=None,year=None,d=None,m=None,y=None):
	companyname = '%s' % (c)
	startdate = '%s-%s-%s' % (day, month, year)
	print startdate
	enddate = '%s-%s-%s' % (d, m, y)
	print enddate"""
	
