# Checking every element in an array against every other
length = len(array)
for idx in range(length):
    for idx2 in range(idx+1, length):
        # a = array[idx] + array[idx2]

# lists & sort
a = [5, 5, 1, 7, 9, 1]
list(set(a))    # remove redundant elements. Note: will automatically sort
sorted(a)       # sort the list

# O(1) search Time! -- use Set instead of lists
# sets and disctionary
# imp: search in set is O(1) just like a dictionary. Dictionary's retrieval is also O(1)
my_set = {1, 2, 3}    # initializing a non-empty set
3 in my_set         # True   
my_set.add(4)       # add element. Remember: set does not store duplicates
my_set.remove(2)    # remove an element
a = set()           # initialziing empty set
# IMP:
b = [7, 4, 5, 6, 5]
my_set = set(b)     # creating a set from a list # O: {4, 5, 6, 7} 
# Note that the conversion to set also sorts the elements! Also this happens in O(n) time. Iterating through each element and each to a hash set: https://stackoverflow.com/questions/34642155/what-is-time-complexity-of-a-list-to-set-conversion
# i.e. you can sort in O(n) using this concept! (possibly Radix sort type working) -- basically it creates a hash entry for every element -- But can practically be used only for limited size of arrays as after a while it will lead to collision in hash key and it will no longer be a constant access time
# Conclusion: can try this method for small test cases


# for in reversed
for i in reversed(range(5)):
    print(i)    # 4,3,2,1,0

# for with step
for i in range(10, 4, -2):  # start, stop, step :: until [element > stop]
    print(i)    # 10,8,6   

# list comprehension

# join list elements into one string element
a = ['a', 'b', 'c', 'd']    # implode lists or join
''.join(a)                  # imp: remember that this only works with string elements. Not woth int. To make it work for int, type cast
# o: 'abcd'
''.join([str(elem) for elem in a])     # when a has int elements

# dictionaries
# get "key" value or return "default" if key doesn't exist
dict.get("key", "default") 

# similar to get but also sets the default in dictionary along with returning it
dict.setdefault("key", [])     

# remove and return if "key" exists. If not return "default"
del dict["key"]
# or
dict.pop("key", "default")     

# sort dictionary in descending order and return a list
d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

# character manipulation
ch = 'a'
x = chr(ord(ch) + 2) # x -> c

# BINARY
# convert an integer number to binary
"{0:b}".format(9) # O: 1001 : Useful when questions like create a superset of an array eg. [2,3,4] : [[2], [3], [4], [2,3], [3,4], [2,4], [2,3,4], None] i.e 8 sets and you can use binary representations from 1 (001) -> 7 (111) to get all these sets. Although the complexity will be 2^n 
bin(4) # O: '-0b100'    # notice that the response is binary. it has this 0b thing appended in beginning
bin(~4) # O: '-0b101'   # 2's complement 

# convert binary to int
int('101', 2)   # O: 5

# get complement (reverse. Not 2's complement. For 2's complement simply use ~ on a decimal numbner)
''.join([str((int(c) ^ 1)) for c in "0011"]) # o: 1100 # approach: XOR each bit by 1 and save. join list to string. type castings used because iteration only works on string, but XOR only works on number and join only works on string


# get all subsets of a set of size n
import itertools
list(itertools.combinations([1, 2, 3], 2)) # get all subsets with 2 elements
# get all permuations of size n
from itertools import permutations
list(permutations(['1','2','3'],2)) # (1,2) != (2,1)

# mapping
[i * 2 for i in range(10) if i * 2 > 4]
# o: [6, 8, 10, 12, 14, 16, 18]

# conditional
print("Safe" if 2 < 1 else "Unsafe")
# o: Unsafe

# lambda
# TODO

# map
# TODO

# filter
# TODO

# date
import datetime
datetime.datetime.strptime('15:30','%H:%M') # change string to time
datetime.datetime.now()     # get current time
# also time objects can be compared directly