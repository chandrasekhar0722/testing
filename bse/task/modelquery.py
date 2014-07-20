from task.models import *


class task():
	
	def tasktesting(self):
	    data = Company.objects.all().values()
	    return data	
