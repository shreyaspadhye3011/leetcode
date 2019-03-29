# uses unnecessary space for swap. temp buffer. but that swapping or choice of larger array can be made in a multitude of ways. Use, but mention in interview
# to avoid - just call same function with reversed parameters in place of swap

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

        while i < len(a1):
#             sec = (0, a2[i]) [i < len(a2)] # Reference (ternary operator): http://book.pythontips.com/en/latest/ternary_operators.html
            if i < len(a2):
                sec = a2[i]
            else:
                sec = 0
            result = a1[i] + sec + carry
            res.append(int(result % 10))
            carry = int(result / 10)
            i += 1
        
        if carry > 0:
            res.append(carry)
            
        print res
    
        return res


obj = addTwoNum()
obj.addTwoArrays([2, 9, 9], [8]) 
# obj.addTwoArrays([5, 9, 2], [3, 1, 5, 3]) # 8083 -- o/p will be rev of this. remember that the numbers are read backwards -- given in problem
# obj.addTwoArrays([2, 9, 9], [8]) # 1000
# addTwoNumbers([2, 4, 3], [5, 6, 2]) # A: 706
# addTwoNumbers([2, 4, 3], [5, 6]) # A: 407
# addTwoNumbers([2, 8, 9, 2], [8]) # A: 2990
# addTwoNumbers([9, 9, 9, 1], [1]) # A: 2000
# addTwoNumbers([0, 0, 8, 2], [0, 0, 2]) # A: 3000