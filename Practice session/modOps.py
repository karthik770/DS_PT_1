# Exercise 1: 
# step 1:Create a Module for Logical Operators , Bitwise Operators,Membership Operators,Identity Operators 
# with different functions/ methods 
# step 2: Create a program to give inputs for each functions and print the output


def Logical(x,y):
    print('x and y is',x and y)
    print('x or y is',x or y)
    print('not x is',not x)

def Bitwise(a,b):
    print("a & b =", a & b)
    # Print bitwise OR operation
    print("a | b =", a | b)
    # Print bitwise NOT operation
    print("~a =", ~a)
    # print bitwise XOR operation
    print("a ^ b =", a ^ b)
    # Binary Left Shift
    print ("a << 1 : ", a<<1)
    # Binary Right Shift
    print ("a >> 1 : ", a>>1)

def Membership(x,y):
    print(x in y)
    print(x not in y)

def identity(a,b):
    print(a is not b)
    print(a is b)



