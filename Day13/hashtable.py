thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["registrationdate"]="04/01/2023"
print(thisdict)

del thisdict["model"]
print(thisdict)

for i in thisdict.keys():
    print(i)