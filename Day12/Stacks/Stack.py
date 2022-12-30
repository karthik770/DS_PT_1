def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item): # ([],'1')
    stack.append(item)
    print("pushed item: " + item)

def pop(stack): # ['1','2','3','4','5']
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop() # ['1','2','3','4']

stack = create_stack() #--> stack =[]
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
