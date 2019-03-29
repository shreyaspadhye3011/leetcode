# Reference (ternary operator): http://book.pythontips.com/en/latest/ternary_operators.html

class addTwoNum:
    #Todo: add code to work on lists
    def addTwoArrays(self, l1, l2):
        # a1 = listTo Array(l1)
        # a2 = listTo Array(l2)
        a1 = l1
        a2 = l2
        if len(a2) > len(a1):
            temp = a1
            a1 = a2
            a2 = temp

        carry = 0
        res = []
        i = 0

        # while i < len(a1):
        #     sec = 


obj = addTwoNum()
obj.addTwoArrays([3, 1, 5], [5, 9, 2, 2])

# addTwoNumbers([2, 4, 3], [5, 6, 2]) # A: 706 -> O: 6 -> 0 -> 7 
# addTwoNumbers([2, 4, 3], [5, 6]) # A: 407
# addTwoNumbers([2, 8, 9, 2], [8]) # A: 2990
# addTwoNumbers([9, 9, 9, 1], [1]) # A: 2000
# addTwoNumbers([0, 0, 8, 2], [0, 0, 2]) # A: 3000