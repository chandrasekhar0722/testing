from task.modelquery import task


class service():

	def __init__(self):
		self.query = task()

	def csv(self):
            csv = self.query.tasktesting()
            return csv

	def saving(self,price):
            saving = self.query.savecsv(price)
            return csv
