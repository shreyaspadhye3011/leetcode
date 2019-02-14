#
# Complete the 'cutSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY lengths as parameter.
#
def cutTheSticks(A):
    # Write your code here
    # A = []
    output = []
    # for i in lengths:
    #     A.append(i)
    output.append(len(A))

    while len(A) > 0:
        to_remove = min(A)
        A = list(filter(lambda a: a != to_remove, A))
        A[:] = [x - to_remove for x in A]
        if len(A) != 0:
            output.append(len(A))
    
    return output