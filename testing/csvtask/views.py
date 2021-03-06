from csvtask.models import *
import csv
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from csvtask.service import service
csv_filepathname="/usr/local/testing/task/EQ140214.CSV"

def import_db(request):
   
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    for row in dataReader:
	if row[0] != 'SC_CODE': # Ignore the header row, import everything else
		data = Company()
		data.sc_code = row[0]
		data.companyname = row[1]
		data.save()
		data2 = Companydetail()
		data2.company = data
		data2.open = row[4]
		data2.high = row[5]
		data2.low = row[6]
		data2.close = row[7]
		data2.last = row[8]
		data2.prevclose = row[9]
		data2.no_trades = row[10]
		data2.no_of_shirs = row[11]
		data2.net_turnov = row[12]
		data2.date = row[14]
		data2.save()
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
