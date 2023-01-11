import pandas 
import numpy 
data ={
    'Name': ['S1','S2','S3','S4','S5','S6'],
    'Marks':[75,80,90,45,99,100],
    'Gender':['M','F','F','M','F','M']
}
Missingdata ={
    'Name': ['S1','S2','S3','S4','S5','S6'],
    'Marks':[75,80,90,numpy.nan,99,numpy.nan],
    'Gender':['M','F','F','M','F','M']
}
 
a= pandas.DataFrame(Missingdata)
print(a.isnull())
#Handle the Null or missing value 
# 1. Deleting 
# 2.Fill that with another value
#print(a.dropna()) #--Deleting
print(a.fillna(0))
#print(a)
