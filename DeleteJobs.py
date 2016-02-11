#-------------------------------------------------
#--- Delete All Job Files
#-------------------------------------------------

import os

def DeleteJobs():
	ActivePath = os.path.dirname(os.path.abspath(__file__))
	for filename in os.listdir(ActivePath):
		if filename.find(".job") > 0:
			os.remove(filename)
		elif filename.find(".bat") > 0:
			os.remove(filename)
			
if __name__ == '__main__':
	DeleteJobs()