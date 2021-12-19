This is the github repository for the 5th semester nanotechnology 2021 project by:
Jacob Koch
Christian Damsgaard Nielsen
Joachim Bach
Tobias Winckler-Carlsen
Mark Buje Hein Sørensen
Yalda Khoja

# Features
The repository is split into two parts, Error correction and simulations.
The error correction folder holds the error correction script, .py file and data from several error correction runs.  The folder is further split up into T18D+G82R, T80D, and WT folders. These contain 8 folders each in which the output of each error correction run has been stored. 
-The files are named as:
>'Mutant'-'bond'-'error correction range'

-Example:
>WT-OH-1


The simulations folder contains....


## Error correction script
Here you will find the Error correction script and .py files.
-The script requires a folder with ONLY a folder named 'data'.
-In the folder the .csv files format data should be entered.
This .csv file need 2 rows.
When running the .exe file a cmd promt will appear and ask for the following:
-Point: 
>This is the point where absorbance values should be read for each spectrum from t=0 to t=37.
>
 -Start point of window: 
 >This is where the first data entry point of the error correction range M1 should be entered.
 >
 -End point of window:
 >This is where the last data entry point of the error correction range M2 should be entered.

-The math run by the script:
$$R_m=\frac{\underset{\text{n=M1}}{\overset{\text{M2}}{\sum}} (x_m[n]-x_0[n])}{\text{M2}-\text{M1}}$$
$$y_m[n]=x_m[n]-R_m $$ 

-The script then plots a graph of all corrected spectra on top of each other in a window along with, a graph of, both the corrected and uncorrected absorbance point chosen against the number of .csv files the point was found in.

-The script also plots a graph of just the uncorrected absorbance point chosen against the number of .csv files the point was found in.

-The script also prints all $R_m$ values found during the run along with, all data points of the corrected and uncorrected absorbance point chosen. 

-The script creates a folder named 'correctedData' in the same directory as its own location. This contains a folder named 'data'. where .csv files for all corrected spectra during that run are created.
