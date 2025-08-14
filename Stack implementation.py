# Stack implementation 
 
def push(stack, ele):
    stack.append(ele)
    print(ele, "inserted into stack successfully")
 
def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
        return 
    print(stack[-1], "deleted successfully")
    stack.pop()
 
stack = [] 
push(stack, 10)
push(stack, 20)
# [10, 20]
push(stack, 30)
push(stack, 40)
# [10, 20, 30, 40]
 
pop(stack)
# [10, 20, 30]
pop(stack)
# [10, 20]
pop(stack)
# [10]
pop(stack)
# []
pop(stack)
# []