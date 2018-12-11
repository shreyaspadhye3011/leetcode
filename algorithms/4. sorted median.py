# pre-requisite: Both arrays are sorted, given
import statistics
# A = [2, 3]
A = [1, 2, 3] 
B = [7, 8, 9, 10, 11]
len_A = len(A)
len_B = len(B)

# consider A to always have the smaller array. If not, swap
if len_B < len_A:
    temp = A
    A = B
    B = temp

# case A: when the smaller array that is appended (A) has all elements smaller to the larger array
if A[-1] < B[0]:
#     median_offset = float(len_A) / 2
    median_offset = len_A / 2.0
    
C = A + B
print(C)
print(statistics.median(C))
print(median_offset)