# Problem: Implement 3 stacks in one array & keep min (3.1 + 3.2)
# Solution: Create push, pop, length functions for all 3 stacks and this should solve our purpose
import math
# TODO: Add check condition on pop when there's nothing in stack to respond with a message
class stackinarr:
    def __init__(self, A=[[], [], []]):
        self.A = A 
        self.min = math.inf        # considered only positive numbers

    def push1(self, item):
        if item < self.min:
            self.min = item
        self.A[0].append(item)

    def pop1(self):
        self.A[0].pop()

    def push2(self, item):
        if item < self.min:
            self.min = item
        self.A[1].append(item)

    def pop2(self):
        self.A[1].pop()

    def push3(self, item):
        if item < self.min:
            self.min = item
        self.A[2].append(item)

    def pop3(self):
        self.A[2].pop()

    def show(self):
        return self.A

    def showMin(self):
        return self.min

obj = stackinarr()
obj.push1(23)
obj.push1(1)
obj.push1(4)
obj.push2(2)
obj.pop1()
obj.push2(13)
obj.push2(2)
obj.push2(4)
obj.push3(6)
obj.push3(7)
obj.pop3()
obj.pop2()
obj.show()
obj.showMin()
    

