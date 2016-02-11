# HTCondor-EnergyPlus

## Description
Simple GUI written in Python to run EnergyPlus simulations on a HTCondor pool using a simple csv file as input.

## Notes
The program works but some more development is planned. Here are a few ideas:
+ Use the HTCondor Python bindings instead of having to create a *.job file for each individual job
+ Add a visualation tab to be able to show the results of the `condor_status` and `condor_q` command

## Instructions
1. Create a csv file similar to JobTemplate.csv present on the repo (keep the headers)
2. Run HTCondor-EnergyPlus.py
3. Select your csv file
4. Click on the Submit button to submit your job(s) to your HTCondor pool
5. Click on Delete to delete the *.job and *.bat file(s)

