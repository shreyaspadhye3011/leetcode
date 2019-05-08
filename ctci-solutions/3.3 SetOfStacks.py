# Imagine a (literal) stack of plates If the stack gets too high, it might topple Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold Implement a data structure SetOfStacks that mimics this SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity SetOfStacks push() and SetOfStacks pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack)
# FOLLOW UP: Implement a function popAt(int index) which performs a pop operation on a specific sub-stack

class SetOfStacks:
    def __init__(self, A=[[]], currentPos=0, limit=2):
        self.A = A
        self.currentPos = currentPos
        self.limit = limit
    
    def push(self, item):
        if len(self.A[self.currentPos]) > self.limit:
            self.A.append([item])
            self.currentPos += 1
        else:
           self.A[self.currentPos].append(item)

    def pop(self):
        if self.currentPos == 0 and len(self.A[self.currentPos] == 0):
            return "No items left in the SetOfStacks"
        if len(self.A[self.currentPos]) == 1:
            self.A[self.currentPos].pop()
            del self.A[self.currentPos]
            self.currentPos -= 1
        else:
            self.A[self.currentPos].pop()
    
    def show(self):
        return self.A

obj = SetOfStacks()
obj.push(3)
obj.push(4)
obj.push(7)
obj.push(1)
obj.push(2)
obj.push(4)
obj.push(6)
obj.push(9)
obj.push(0)
obj.show()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.show()