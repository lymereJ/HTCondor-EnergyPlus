#-------------------------------------------------
#--- Create Job to Run Energyplus with HTCondor
#-------------------------------------------------

def CreateJob(JobName,BatchFile):
	JobFile = open(JobName + ".job","w")
	JobFile.write("## HTCondor Job; Running EnergyPlus; Batch file: " + BatchFile + ".bat\n\n")
	JobFile.write("UNIVERSE = Vanilla \n")
	JobFile.write("EXECUTABLE = " + BatchFile + ".bat\n")
	JobFile.write("QUEUE")

if __name__ == '__main__':
	CreateJob(JobName,BatchFile)
