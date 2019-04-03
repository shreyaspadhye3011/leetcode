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
        
        return tot

obj = zigzag()
obj.find_zigzag("PAYPALISHIRING", 3)
            