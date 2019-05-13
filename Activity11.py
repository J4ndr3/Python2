import pandas as pan
from pandas import DataFrame
import numpy as nump
import matplotlib.pyplot as plt
import matplotlib.animation as pla

# 1. Import the data from your CSV file into a Pandas Dataframe
titan = pan.read_csv("mpg.csv")
print("1. Import the data from your CSV file into a Pandas Dataframe\n")
print(titan,"\n")
# 2. Add a new calculated column to the dataframe
titan['Mile per gallon vs Acceleration']= titan['mpg']/titan['acceleration']
print("2. Add a new calculated column to the dataframe\n")
print(titan,"\n")
# 3. Create a subset of the data based on a condition
titaneurope = titan[titan['origin'] == 'europe']
print(" 3. Create a subset of the data based on a condition\n")
print(titaneurope,"\n")
# 4. Calculate the correlation coefficient between two columns and show whether a significant
#  correlation exists (correlation coefficient values less than +0.8 or greater than -0.8 are
#   not considered significant).
titanMA = pan.read_csv("mpg.csv",usecols = ['mpg','acceleration'])
np_titan=nump.array(titanMA)
npt=nump.corrcoef(np_titan[:,0],np_titan[:,1])
print("4. Calculate the correlation coefficient between two columns.\n")
print(npt,"\n")
r=npt[0,1]
if npt[0,1] < 0.8:
    if npt[0,1] > -0.8:
        print("show whether a significant correlation exists\n")
        print("The correlation",r," is not significant\n")
else:
    print("show whether a significant correlation exists\n")
    print("The correlation",r," is significant")
# 5. Generate a data visualisation from the data in your data frame. Your visualisation must be
# sensibly thought out (i.e. answer a reasonable business question) and it must have customised
# styling (e.g. title, axis labels, legend, colors, etc.)
titanMAS = titan.sort_values(['weight','horsepower'])
print(titanMAS)
plt.scatter(titanMAS['weight'],titanMAS['horsepower'],color='green')
plt.xlabel("Horsepower")
plt.ylabel("Weight")
plt.title("The effecty of weight on horsepower")
plt.show()