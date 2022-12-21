class ArithmeticOperations:
    def __iter__(self):
        self.a= 1
        return self
    
    def __next__(self):
        i=self.a
        self.a= self.a+1
        return i

AO= ArithmeticOperations()
AI = iter(AO) # ---> Exact function of For loop 
print(next(AI))