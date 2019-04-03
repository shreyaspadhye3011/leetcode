class zigzag:
    def find_zigzag(self, s, numRows):
        tot = []
        key = 0
        for char in s:
            if key < len(tot):
                tot[key].append(char)
            else:
                tot.append([char])
                
            if key == 0:
                change = 1
            elif key == numRows - 1:
                change = -1
                
            key += change
            
        str = ""
        # Though looks like n**2 complexity but won't be as the number of times this loop will work will br n - for every element
        for charList in tot:
            for c in charList:
               str += c
        return str

obj = zigzag()
obj.find_zigzag("PAYPALISHIRING", 4) #O: PINALSIGYAHRPI
obj.find_zigzag("PAYPALISHIRING", 3) #O: PAHNAPLSIIGYIR
obj.find_zigzag("PAY", 3) #O: PAY
obj.find_zigzag("PAY", 4) #O: PAY
obj.find_zigzag("PAY", 2) #O: PYA
            