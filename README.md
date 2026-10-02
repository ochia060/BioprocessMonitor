# Bioprocess Monitor
A Python based monitoring tool that analyses batch fermentation data and generates dashboards and summary tables for pH, temperature, and component concentration.

## Overview:
The goal of this project was to develop a Python based tool for monitoring fermentation processes using batch data.
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
 <img width="5200" height="3200" alt="Batch_001_Mode_A" src="https://github.com/user-attachments/assets/0f229e26-d363-4da8-adaa-26fb561a9041" /> \
\
The dashboard provides an overview of the process conditions for a single fermentation batch. It contains 4 scatter plots demonstrating species concentration (top left), temperature (top right), pH (bottom left), and %dissolved oxygen (bottom right) over time.


## Summary Table
|batch_id|ph_optimal_percent|temperature_optimal_percent|C_product_g_L^-1_final|
|--------|------------------|---------------------------|----------------------|
|1       |93.81             |97.94                      |46.5                  |
|2       |96.69             |97.52                      |50.8                  |
|3       |95.89             |93.15                      |44.6                  |
|4       |100.0             |96.47                      |48.6                  |
|5       |48.62             |99.08                      |24.7                  |
--------------------------------------------------------------------------------

The summary table provides an overview of the %of pH and temperature measurements within optimal operating range, and the final glucose concentration. It shows this for each batch, and each operation mode.

