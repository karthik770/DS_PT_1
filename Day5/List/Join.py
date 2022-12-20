List1=['a','b','c','d','e']
List2=[1,2,3,4,5]

# + Operator

List3= List1+ List2
print("+ Operator")
print(List3)

# Append ()

List4=[]
for i in List2:
    List1.append(i)
   # List1.append(List2)
List4=List1.copy()
print("Append()")
print(List4)

#Extend()

List1.extend(List2)
print("Extend()")
print(List1)