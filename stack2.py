class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,item):
        self.stack.append(item)
        print(f"Pushed:{item}")
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return f"Popped:{self.stack.pop()}"
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return f"Top:{self.stack[-1]}"
    
    def is_empty(self):
        if len(self.stack)==0:
            print("Stack is empty")
            
    def size(self):
        return len(self.stack)
    
    def display(self):
        print("Stack from top to bottom",self.stack[::-1])
            
   
s=Stack()
s.push(int(input("enter a number")))
s.push(20)
print(s.peek())
s.push(30)
s.display()
print(s.pop())
print(s.peek())

print(s.is_empty())
s.display() 