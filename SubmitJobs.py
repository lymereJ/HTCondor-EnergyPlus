#-------------------------------------------------
#--- Submit Batch Files to HTCondor
#-------------------------------------------------

import os
import subprocess

def SubmitJobs():
	ActivePath = os.path.dirname(os.path.abspath(__file__))
	for filename in os.listdir(ActivePath):
		if filename.find(".job") > 0:
			subprocess.call(["condor_submit",filename])

if __name__ == '__main__':
	SubmitJobs()