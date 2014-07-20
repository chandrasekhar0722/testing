import csv
from django.shortcuts import render_to_response,HttpResponse,render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from task.service import service
from task.models import Company,Companydetail
import os
import json
from django.utils import simplejson

# Create your views here.
csv_name = 'EQ180714.CSV'
csv_filepathname="/usr/local/bse/csv/%s" % csv_name


csv_date = csv_name[2]+csv_name[3]+'-'+csv_name[4]+csv_name[5]+'-'+'20'+csv_name[6]+csv_name[7]

def index(request):
	return render_to_response('home.html')


def import_db(request):
   
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    for row in dataReader:
	if row[0] != 'SC_CODE': # Ignore the header row, import everything else
		data = Company()
		data.code = row[0]
		data.companyname = row[1]
		data.sc_group = row[2]
		data.sc_type = row[3]
		data.save()
    return HttpResponseRedirect('/')

def stockdata(request):
    es = service()
    
    values = es.csv()
    for i in values:
	code = i['code']
    #print values[0]['code']
    dataReader1 = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    for row1 in dataReader1:
	if row1[0] != 'SC_CODE': # Ignore the header row, import everything else
		data = Companydetail()
		data.sc_name = row1[0]
		data.opening = row1[4]
		data.high = row1[5]
		data.low = row1[6]
		data.close = row1[7]
		data.last = row1[8]
		data.prevclose = row1[9]
		data.no_trades = row1[10]
		data.no_of_shirs = row1[11]
		data.net_turnov = row1[12]
		data.date = csv_date
		data.save()
    return HttpResponseRedirect('/')


def getdata(request,code=None,day=None,month=None,year=None):
	code = '%s' % (code)
	date = '%s-%s-%s' % (day, month, year)
	a = Company.objects.filter(code=code).values()
	for i in a:
		b = list(Companydetail.objects.filter(date=date,sc_name=i['code']).values('opening','close'))
	return HttpResponse(simplejson.dumps(b,indent=2), content_type='application/json') 

def getdatabetweentwodate(request,c=None,day=None,month=None,year=None,d=None,m=None,y=None):
	companycode= '%s' % (c)
	startdate = '%s-%s-%s' % (day, month, year)
	enddate = '%s-%s-%s' % (d, m, y)
	company_detail = Company.objects.filter(code=companycode).values()
	
	for i in company_detail:
		company_data = list(Companydetail.objects.filter(sc_name=i['code'],date__range=(startdate,enddate)).values('opening','close'))
		result = json.dumps(company_data)
	return render_to_response('graph.html', {"result": result})
