# HTCondor-EnergyPlus

## Description
Simple GUI written in Python to run EnergyPlus simulations on a HTCondor pool using a simple csv file as input.

## Notes
The program works but some more development is planned. Here's a few ideas:
+ Using the HTCondor Python bindings instead of having to create a *.job file for each individual job
+ Add a visualation tab to be able to show the results of the `condor_status` and `condor_q` command

## Instruction
1. Create a csv file similar to JobTemplate.csv present on the repo. The headers are needed
2. Run HTCondor-EnergyPlus.py
3. Select your csv file
4. Click on the Submit button to submit your job to your HTCondor pool
5. Click on Delete to delete the *.job and *.bat files

