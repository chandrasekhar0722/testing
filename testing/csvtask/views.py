from csvtask.models import *
import csv
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from csvtask.service import service
csv_filepathname="/usr/local/testing/task/EQ120214.CSV"

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
		data.open = row1[4]
		data.high = row1[5]
		data.low = row1[6]
		data.close = row1[7]
		data.last = row1[8]
		data.prevclose = row1[9]
		data.no_trades = row1[10]
		data.no_of_shirs = row1[11]
		data.net_turnov = row1[12]
		#data.date = row1[14]
		data.save()
    return HttpResponseRedirect('/')
