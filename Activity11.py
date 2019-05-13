import pandas as pan
from pandas import DataFrame
import numpy as nump

titan = pan.read_csv("mpg.csv")
print(titan)
titan['Mile per gallon vs Acceleration']= titan['mpg']/titan['acceleration']
print(titan)

titaneurope = titan[titan['origin'] == 'europe']
print(titaneurope)