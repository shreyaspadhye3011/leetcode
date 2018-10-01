# Source: https://leetcode.com/problems/fruit-into-baskets/
# Author: Shreyas Padhye
# Algorithm:
# Percentile: Wrong Answer in [0,1,6,6,4,4,6]

def calculateMaxSelection(A):
    max = 0
    currentSet = []
    currentSet.append(A[0])
    count = 1
    numLast = A[0]
    countLast = 0

    for i in range(1, len(A)):
        if (A[i] in currentSet):
            count += 1
            if (A[i] == numLast):
                countLast += 1
            else:
                numLast = A[i]
                countLast = 1
        elif (len(currentSet) != 2):
            currentSet.append(A[i])
            count += 1
            
            numLast = A[i]
            countLast = 1
        else:
            currentSet[0] = A[i-1]
            currentSet[1] = A[i]
            if (count > max):
                max = count     
            count = 1 + countLast
    if(count > max):
        return count
    else:
        return max

# calculateMaxSelection([1,2,1,3,4,3,5,1,2])   #O: 3
# calculateMaxSelection([1,2,1,3,3,3,3,1])   #O: 5
# calculateMaxSelection([1,1,2,2,3,2,2,3])   #O: 6 -> [2,2,3,2,2,3]
# calculateMaxSelection([0,1,6,6,4,4,6])   #O: 6