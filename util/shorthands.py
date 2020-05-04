# Conversion / casting
int(5.3)    # 5
float(5)    # 5.0
int("12")   # 12
float("12")   # 12.0

# Formating strings
"I am a {} {}".format("disco", "dancer")

# check whether a number is prime or not. Just call this number inside a loop of k if you want to find k prime numbers
def isPrime(number):
    divisor = 2 
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

# Checking every element against every other upcoming number in an array
length = len(array)
for idx in range(length-1):
    for idx2 in range(idx+1, length):
        # a = array[idx] + array[idx2]

# for each with both index and value
for idx, val in enumerate(ints):
    print(idx, val)

# int max & minimum possible value
import sys
max = sys.maxsize       # 9223372036854775807
min = -sys.maxsize - 1  # -9223372036854775808

# ----------------------- LISTS --------------------------- #

# list append, insert, pop & remove
list1 = [ 1, 2, 3, 4, 5, 6]
list1.append(7)     # [1, 2, 3, 4, 5, 6, 7] # append
# insert 10 at 4th index  
list1.insert(4, 10)  # [1, 2, 3, 4, 10, 5, 6, 7]
a.pop()   # removes the last element of the array i.e O(1)
# Note: Lists behave as Stacks by default
a.pop(0)  # remove first element from the array ~ O(N) complexity. pop(k) has O(k) complexity in python
a.remove(value)   # remove first value from list that matches the given value

# lists & sort
a = [5, 5, 1, 7, 9, 1]
list(set(a))    # remove redundant elements. Note: will automatically sort
a.sort()        # sort the original list
a.sort(reverse=True)    # descending
sorted(a)       # return a sorted version of the list. #IMP: The original list doesn't change. Basically, can be used for iterating
sorted(a, reverse=True) # descending

# list slice
a = [2, 3, 4, 5, 6]
# <start_from : stop_at : reverse>
a[1:4]  # [3, 4, 5] -> [strtIdx:endIdx] :: strtIdx(inclusive) -- endIdx(excluding)
a[1:]   # [3, 4, 5, 6]
a[:3]   # [2, 3, 4]
a[::-1] # [6, 5, 4, 3, 2]
# IMP: Remeber that slicing is an O(N) space and time intensive operation. Don't end up using it inside a for loop multiple times just because it's convenient. It'll shoot up your complexity even though your code looks neat and less in number of operations
max_array = [2, 3, 4, 5]
# print last 3 numbers
max_array[-3:]          # [3, 4, 5]
# print last 3 numbers, reverse
max_array[:-4:-1]       # [5, 4, 3]
# print first 3 numbers, reverse
    max_array[2::-1]    # [4, 3, 2] -> <start_from:stop_at:reverse=True> = note that it started from back, from index 2 and printed the whole list as no end given so it prints till start
    # Similarly, skip first and print 2, reverse
    max_array[2:0:-1]   # [4, 3] -> <start_from:stop_at:reverse=True>
# Note: with -1, indexing remains same, just direction of traversal changes
# Note: stop_at is always excliusive, i.e. that index will NOT be included in the sliced array

# ----------------------- LIST SECTION ENDS --------------------------- #

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
# Set Difference
set1 = {1, 3, 5, 6}
set2 = {3, 5}
set1 - set2 # {1, 6}
set2 - set1 # set() -> empty set
list(set1)  # create list from a set

# Queues
# Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.
# Reference: https://medium.com/@shuangzizuobh2/how-well-do-you-code-python-9bec36bbc322
# Reference: https://docs.python.org/2/library/collections.html#collections.deque 
deque(['f', 'g', 'h', 'i', 'j'])
d.pop()         # 'j'   O(1)
d.popleft()     # 'f'   O(1)
# Note: Both are O(1) because these are built on top of linked list implementations (pointers to both ends) along with array concepts of contiguous memory for quick retrieval -- A very high level understanding
# Note: Both stacks / lists and queues support ppek() operation which just looks at the top or last element respectively without removing it

# for in with reversed index
for i in reversed(range(5)):
    print(i)    # 4,3,2,1,0

# for with step
for i in range(10, 4, -2):  # start, stop, step :: until [element > stop]
    print(i)    # 10,8,6   

# strings in python
# strings in C are mutable i.e. you can add strings in constant time because they are implemented as array of characters under the hood and constant time append is possible in dynamic arrays
# But strings in Python, Java, JavaScript, Golang are IMMUTABLE!
# i.e when you do something like `str1 + str2` -- it is actually a copy operatiom of cost O(n+m) where both strings are copied to new location that represent the new resultant string
# Therefore, when you have lot of string manipulation involved, change the string to actual array of characters before working (mutating) on it
# You can use functions like split() to do this

# replace a substring in a given string
string = "node in node node"  
print(string.replace("node", "Node"))  # Node in Node Node

# Flatten array: join list elements into one string element
a = ['a', 'b', 'c', 'd']    # implode lists or join
''.join(a)                  # imp: remember that this only works with string elements. Not woth int. To make it work for int, type cast
# IMP - join only works for char elements and NOT for integers
# For int array, use:
ch = ''
for i in a:
    ch += i
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

# initialize a dictionary : defaultdict
from collections import defaultdict
wordlist =["a", "a", "b"]
word_count = defaultdict(int)
for w in wordlist: 
  word_count[w] +=1

# character manipulation
ch = 'a'
x = chr(ord(ch) + 2)    # x -> c
'l'.upper()             # L
'A'.lower()             # a
# .islower()
# .isupper()

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

# Dynamic Arrays: amortized analysis
# Reference: AlgoExpert
# 1. Lists in Python or arrays in JavsScript are dynamic arrays underhood
# 2. For static arrays, increasing array size, inserting in  middle or end or front is O(N) time & O(1) space: Process: copy the whole array to a new location which can hold the updated size of the array. Array is always contiguous memory blocks. O(1) space because the old space is cleared once copied
# 3. To solve, this we use dynamic array which does two things:
    # a. Allocate 2 * N size during init
    # b. While appending (in the end), if you run out of space, always add 2 * N new blocks (by same copy method as static array). Therefore, whenever you run out of space, you give yourself double the space. Thus, giving constant time insertions for a long time as space is available and no copy / shift is required
    # This leads to an amortized complexity of O(1) for append in dynamic arrays. Notice that the worst case when you run out of memory is taking O(N) time but OVERALL the constant time insertions dominate. Therefore, O(1)
# 4. Note that insertion at front or middle is still O(N) in case of dynamic array. though the extra double init space does help but you need to always perform SHIFT operation for insertion in front or middle

# JSON handling
# Reading a JSON file as dictionary
with open('distros.json', 'r') as f:
    distros_dict = json.load(f)
for distro in distros_dict:
    print(distro['Name'])

# parsing JSON
parsed_json = (json.loads(json_data))

# extra
print(json.dumps(parsed_json, indent=4, sort_keys=True))
loaded_json = json.loads(json_data)
for x in loaded_json:
	print("%s: %d" % (x, loaded_json[x]))

pattern = ""
if (pattern):
  print("will not reach")  # will not print 

min = a if a < b else b     # ternary operator

# do while
# python does not have `do while`, use:
    while True:
        if (condition):
            break

