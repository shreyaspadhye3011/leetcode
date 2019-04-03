class zigzag:
    def find_zigzag(self, s, numRows):
        tot = []
        key = 0
        for char in s:
            if key < len(tot):
                tot[key].append(char)
            else:
                tot.append([char])
                
            if key == numRows - 1:
                change = -1
            elif key == 0:
                change = 1
                
            key += change
        
#         tot.join('', for c in tot)
        str = ""
        for charList in tot:
            for c in charList:
               str += c
        print str

obj = zigzag()
obj.find_zigzag("PAYPALISHIRING", 4) #O: PINALSIGYAHRPI
obj.find_zigzag("PAYPALISHIRING", 3) #O: PAHNAPLSIIGYIR
            