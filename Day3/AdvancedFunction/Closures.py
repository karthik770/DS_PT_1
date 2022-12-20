def outerFunction(num):
 
    def innerFunction():
        print(2*num)
    return innerFunction
 
if __name__ == '__main__':
    myFunction = outerFunction(5)
    myFunction()