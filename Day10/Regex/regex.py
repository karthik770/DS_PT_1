import re
txt='unikaksha'
a=re.findall('a',txt)
b=re.search('sha',txt) 
c=re.split('a',txt)
d=re.sub('sha','@', txt)
print(a)
print(b.start())
print(c)
print(d)
