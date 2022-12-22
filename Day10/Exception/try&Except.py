# try:
#     u=0
#     a=10/u
#     print(a)
# except ArithmeticError:
#     print("Arithmetic error --Division is not possible")
# finally:
#     print("Happy Coding !")

# try:
#     a=int(input("Enter a number to find odd or even:"))
#     if(a>10):
#         if(2/a==0): 
#             print("Even Number")
# except TypeError:
#     print("Not a even Number")
# else:
#     print("To find the value of 1/given number")
#     b=1/a
#     print(b)
# finally:
#     print("Happy Coding !")

a=[1,2,3,4] 
try:
    print(a[0])
except:
    print("Index not found")
finally:
    print("Happy Coding !")
