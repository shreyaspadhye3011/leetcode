# Almost similar if same length and character frequency doesn't differ from more than 3 (function working over an array of strings and result as ["YES", "NO", "YES", "YES"] depending on case)
# status: normal cases working but edge cases failing. not sure what were the cases. debug
def areAlmostEquivanlent(s, t):
    dict = {}
    result = []
    rejected = False 
    for i in range(len(s)):
        # check same length
        if len(list(s[i])) != len(list(t[i])):
            result.append("NO")
            continue
            
        # create a count dictionary from characters of first string
        for char in list(s[i]):
            val = dict.get(char, 0)
            dict[char] = val + 1
        
        # deduct count from count dictionary for same characters
        for char in list(t[i]):
            if char in dict:
                dict[char] = dict[char] - 1
            else:
                dict[char] = 1
        
        # at the end no character count should be more than 3
        for val in dict.values():
            if val > 3:
                rejected = True
                result.append("NO")
        
        if not rejected:
            result.append("YES")
            
    return result
        
areAlmostEquivanlent(["ggaa"], ["gfh"]) # len mismatch