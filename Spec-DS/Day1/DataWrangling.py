import pandas 
import numpy 
data ={
    'Name': ['S1','S2','S3','S4','S5','S6'],
    'Marks':[75,80,90,45,99,100],
    'Gender':['M','F','F','M','F','M']
}
data2 ={
    'Name': ['S1','S2','S3','S4','S5','S6'],
    'Interest':['DS','ML','AI','ML','DS','SD']
}
Missingdata ={
    'Name': ['S1','S2','S3','S4','S5','S6'],
    'Marks':[90,80,90,numpy.nan,90,numpy.nan],
    'Gender':['M','F','F','M','F','M']
}
d=pandas.DataFrame(data)
d1=pandas.DataFrame(data2)
a= pandas.DataFrame(Missingdata)
print(a.isnull())
#Handle the Null or missing value 
# 1. Deleting 
# 2.Fill that with another value
#print(a.dropna()) #--Deleting
print(a.fillna(0))
#print(a)

#Reshaping the column Gender 

a['Gender']=a['Gender'].map({'M':0,'F':1})
print(a)
#Filtering
a=a[a['Marks']>=90]
print(a)
# Grouping
grouping=a.groupby('Marks')
print(grouping.get_group(90))

#Merging

d3=pandas.merge(d,d1,on='Name')
print(d3)