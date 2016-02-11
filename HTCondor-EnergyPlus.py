import CreateBatch
import SubmitJobs
import DeleteJobs
import pyforms
import sys
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlFile

class HTCondorEnergyPlus(BaseWidget):
	
	def __init__(self):
		super(HTCondorEnergyPlus,self).__init__('HTCondor & EnergyPlus')

		self._CSVFile 	= ControlFile('CSV File')
		self._Create	= ControlButton('Create')
		self._Submit	= ControlButton('Submit')
		self._Close		= ControlButton('Close')
		self._Delete	= ControlButton('Delete')

		self._formset = ['',('  ','_CSVFile','  '),('', '_Create', '_Submit','_Delete', '' ),('','_Close',''),'']
	
		self._Create.value = self.__CreateAction
		self._Close.value = self.__CloseAction
		self._Submit.value = self.__SubmitAction
		self._Delete.value = self.__DeleteAction
	
	def __CreateAction(self):
		CreateBatch.CreateBatch(self._CSVFile.value)
	
	def __SubmitAction(self):
		SubmitJobs.SubmitJobs()

	def __DeleteAction(self):
		DeleteJobs.DeleteJobs()		
	
	def __CloseAction(self):
		sys.exit()

if __name__ == "__main__":	 pyforms.startApp( HTCondorEnergyPlus )
