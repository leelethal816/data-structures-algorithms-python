from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def reverse_string(string):
    s = Stack()
    for each in string:
        s.push(each)
    reverse = ""
    for i in range(s.size()):
        reverse += s.pop()
    return reverse

print(reverse_string("We will conquere COVID-19"))
print(reverse_string("I am the king"))

def is_balanced(string):
    s = Stack()
    openers = "([{"
    closers = ")]}"
    balanced = True

    for each in string:
        if each in openers and balanced:
            s.push(each)
        else:
            if each in closers and not s.is_empty() and balanced:
                if openers.index(s.peek()) == closers.index(each):
                    s.pop()
            elif each not in openers and each not in closers:
                pass
            else:
                balanced = False

    return balanced


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
