# Source: https://leetcode.com/problems/fruit-into-baskets/
# Author: Shreyas Padhye
# Algorithm: Single Pass. Keep track of a currentSet (a, b) which checks whether the current element can be accepted or not. Also keep a track of the recurring count of previous number's repitition and add that to current count when making curresntState switch [(a, b) -> (b, c)]
# Percentile: 86.63% 	

def calculateMaxSelection(A):
    max = 0                                 # to keep track of max number of collection possible
    currentSet = []                         # to keep track of current basket combination
    currentSet.append(A[0])
    count = 1
    numLast = A[0]                          # to keep track of last recurring element
    countLast = 1

    for i in range(1, len(A)):
        # if it's a type of fruit which is alrady in your basket, just increment count and continue
        if (A[i] in currentSet):
            count += 1
        # if only one of the baskets is occupied, add to second basket
        elif (len(currentSet) != 2):
            currentSet.append(A[i])
            count += 1
        # if both baskets occupied, then start a new combination
        else:
            currentSet[0] = A[i-1]
            currentSet[1] = A[i]
            if (count > max):
                max = count
            count = 1 + countLast
        
        # keep track of recurrence count of last element so that it can be transferred further
        if (A[i] == numLast):
            countLast += 1
        else:
            numLast = A[i]
            countLast = 1
#         print("NumLast: ", numLast, " | CountLast: ", countLast)
    if(count > max):
        return count
    else:
        return max

# calculateMaxSelection([1,2,1,3,4,3,5,1,2])   #O: 3
# calculateMaxSelection([1,2,1,3,3,3,3,1])   #O: 5
# calculateMaxSelection([1,1,2,2,3,2,2,3])   #O: 6 -> [2,2,3,2,2,3]
# calculateMaxSelection([0,1,6,6,4,4,6])   #O: 5