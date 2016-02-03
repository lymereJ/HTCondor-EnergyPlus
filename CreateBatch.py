#----------------------------------------------------
#--- Create a Windows Batch File to Run Energyplus
#----------------------------------------------------

import CreateJob

def CreateBatch(CSVFile):
	CSVFileRead = open(CSVFile).read().split("\n")
	if len(CSVFileRead) > 1:
		for i in range (1, len(CSVFileRead)):
			CSVFileLine = CSVFileRead[i].split(",")
			if CSVFileLine <> "":
				Batch = CSVFileLine[0]
				EnergyPlus = CSVFileLine[1]
				IDF = CSVFileLine[2]
				WeatherFile = CSVFileLine[3]
				BatchFile = open(Batch+".bat","a")
				BatchFile.write(EnergyPlus+" -x -w "+WeatherFile+".epw"+" -p "+IDF+" "+IDF+".idf \n")
				CreateJob.CreateJob(Batch,Batch)
				BatchFile.close()

if __name__ == '__main__':
	CreateBatch(CSVFile)