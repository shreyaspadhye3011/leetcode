def missingWords(s, t):
    res = []
    frstArr = s.split(" ")
    scnArr = t.split(" ") 
    i = 0
    j = 0
    
    while(i < len(frstArr) and j < len(scnArr)):
        if frstArr[i] == scnArr[j]:
            i += 1
            j += 1
        else:
            res.append(frstArr[i])
            i += 1
    
    while i < len(frstArr):
        res.append(frstArr[i])
        i += 1
        
    return res

missingWords("I love programming", "love")