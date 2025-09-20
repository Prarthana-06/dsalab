class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


myStack = Stack()

myStack.push('10')
myStack.push('20')
myStack.push('80')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())


print("Size: ", myStack.size())
