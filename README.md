# Bioprocess Monitor
A Python based monitoring tool that analyses batch fermentation data and generates dashboards and summary tables for pH, temperature, and component concentration.

## Overview:
The goal of this project was to develop a Pythin based tool for monitoring fermentation processes using batch data.
Important process variables, including pH and temperature, were evaluated against pre-defined acceptable operating ranges.
This tool also creates visualised data of process variables over time, and summary tables for each operation mode and batch.

## Features:
The BioprocessMonitor class includes functions for fermentation data analysis:\
**Batch extraction:** extracts data corresponding to a specific fermentation batch\
**pH monitoring:** determines which pH measurements are within acceptable operating limits\
**Temperature monitoring:** determines which temperature measurements are within acceptable operating limits\
**Dashboard generation:** creates a dashboard with subplots showing concentration profiles, temperature, pH, and dissolved oxygen over time\
**Summary generation:** calculates the percentage of measurements within acceptable operating limits and records the final product concentration for each batch\

## Technologies used:
- Python 3.14.7
- numpy 2.5.2
- pandas 3.0.5
- matplotlib 3.11.0

## Code design:
When main.py is run, two operation modes (Mode A and Mode B) are defined with temperature and pH operation limits.
For each operation mode, the program creates a dashboard for each batch and exports the file as a .PNG in the 'figures' directory.\
The program also creates a summary table for each batch and operation mode showing the percentage of measurements within acceptable limits, and the final glucose concentration.
These results are exported as a .csv file in the 'tables' directory\
The pH and temperature limits may be modified in the main.py without chaging the BioprocessMonitor class.

## Dashboard
 

## Summary Table


