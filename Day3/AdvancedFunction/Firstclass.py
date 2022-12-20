# def Converttoupper(text):
#     return text.upper()
  
# # print (Converttoupper('Hello'))
  
# CTU = Converttoupper
  
# print (CTU('Hello'))


# def Converttoupper(text):
#     return text.upper()
  
# def Converttolower(text):
#     return text.lower()
  
# def Passarg(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function
#                     passed as an argument.""")
#     print (greeting) 
  
# Passarg(Converttoupper)
# Passarg(Converttolower)




def create_adder(x):
    def adder(y):
        return x+y
    return adder
  
newvar = create_adder(15)
  
print (newvar(10))