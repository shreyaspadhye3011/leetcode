def calculateMaxSelection(A[]):
    max = 0
    currentSet = A[0]
    count = 1
    numLast = A[0]
    countLast = 0

    for i in range(1, len(A) -1):
        
