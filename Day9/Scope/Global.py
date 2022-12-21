a=10 
def GlobalExplain():
	global a
	a=5
	print(a)
	def sum():
		print(a+a)

print("Before Global Keyword")
print(a)
print("After Global Keyword")
GlobalExplain()
print("Outside Global Keyword")
print(a)
