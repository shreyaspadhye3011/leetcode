# TODO:
# Add code to read line by line input from a file

# ----
# Pass by reference (or object sharing) & Pass by Value
# In python: 
# immutable arguments like integers, strings or tuples are passed by value i.e. change inside function to the parameter won't reflect outside
# all other mutable objects like lists, dictionaries etc are passed by reference

# Note: You can result {} dict to control variables that you want to pass by reference.
def parent(arr, str):
  changeValues(arr, str)
  return arr, str

def changeValues(arr, str):
  # array append reflects in parent: Call by reference
  arr.append("yes")
  # string change doesn't change value in parent: Call by Value
  str = "yes"

parent([1,2], "no")     # O: ([1, 2, 'yes'], 'no')
# ----

# Conversion / casting
int(5)          # 5
int(5.3)        # 5
int('12')       # 12
int('12.9')     # Throws ValueError
float(5)        # 5.0
float(5.3)      # 5.3
float('12')     # 12.0
float('12.9')   # 12.9

# Value check catch -- In python True & 1 internally mean same thing
# Be careful when using EXACT value check for Booleans and 0 & 1. 
# eg if you need a value to be exactly 1, check int(value) inside try-catch where value is a valid integer (int, integer wrapped in quotes or a float value)
True == 1           # True : True is same as 1
False == 0          # True : False is same as 0
True in [0,1]       # True : True is same as 1
'True' in [0,1]     # False : string `True` is not as same as True

# check type
type([5, 6, 89]) == list    # True
type(7) == int         # True
isinstance(value, int) # check if a value is of int type -- can use for custom class as well -- need to test

# IMP: check if a string value can be legitimately turned into int eg "6" -> True. "ss" -> False
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

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
        a = array[idx] + array[idx2]

# for each with both index and value
for idx, val in enumerate(ints):
    print(idx, val)

# int max & minimum possible value
import sys
max = sys.maxsize       # 9223372036854775807
min = -sys.maxsize - 1  # -9223372036854775808

import math
math.inf        # inf --> maximum possible value (not int)
# ----------------------- LISTS --------------------------- #

# list append, insert, pop & remove
list1 = [ 1, 2, 3, 4, 5, 6]
list1.append(7)     # [1, 2, 3, 4, 5, 6, 7] # append
# insert 10 at 4th index  
list1.insert(4, 10)  # [1, 2, 3, 4, 10, 5, 6, 7]
a.pop()   # removes the last element of the array i.e O(1)
# Note: Lists behave as Stacks by default
a.pop(0)  # remove first element from the array ~ O(N) complexity. pop(k) has O(k) complexity in python
# Note: use any valid index in place of 0 to remove ith element from start
a.remove(value)   # remove first value from list that matches the given value
# empty, non-empty check
s = []
# check if list is empty
if not s:
    print("works")
# check if list has elements
if s:
    pass
# list difference - based on sets
array = [4, 6, 7]
integer = 7
list(set(array) - set([integer]))
# result: [4, 6] Note: second argument can be any list

# List Concatenation
# Method A: Avoid:
l = [1, 2, 43, 8]
l = l + [7, 6] # O(N) operation! it is concatenating two lists so internally creates a new list
# Result: [1, 2, 43, 8, 7, 6]
# Method B: Better:
l += [7, 6]         # O(1) Adds to same reference in end using extend()
# same as
l.extend([7, 6])    # O(1) complexity as adds at back of same list. doesn't create new reference
# Result: [1, 2, 43, 8, 7, 6]
# https://www.programiz.com/python-programming/methods/list/extend
# https://stackoverflow.com/questions/33191470/difference-in-complexity-of-append-and-concatenate-for-this-list-code

# lists & sort
a = [5, 5, 1, 7, 9, 1]
list(set(a))    # remove redundant elements. Note: will automatically sort
a.sort()        # sort the original list
a.sort(reverse=True)    # descending
sorted(a)       # return a sorted version of the list. #IMP: The original list doesn't change. Basically, can be used for iterating
sorted(a, reverse=True) # descending
# sorting a list of objects
# for more info see: class_design_basics.py or https://docs.python.org/3/howto/sorting.html
word_list.sort(key=lambda x: x.value)   # where value is an attribute of the comprising object in the list
# sort auxiliary array (of indices) based on another array (strings)
sorted_words = ["race", "blink", "oy", "yo", "linkb", "care"].sort()
indices = [0, 1, 2, 3, 4, 5]
indices.sort(key=lambda x: sorted_words[x]) 

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
my_set.discard(2)   # similar to remove. But will not raise an error if 2 doesn't exist in set
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
set1.update(set2) # {1, 3, 5, 6}    # update a set with another set
set1.update([8, 0]) # {0, 1, 3, 5, 6, 8}    # update a set with a list
set1.intersection(set2)
set1.union(set2)
# IMP: Remember that sets are unordered so there's no get(ith-element) function
# but there is pop() which retrieves and removes an element from the set but as set is unordered (internally), you can't be sure which element it will return
# Think? : Is there a scope of implementing a set like DS which also implements indexing or at least ordered pop - think in terms of questions like findCommonAncestors where rather thatn going with the logic of getting ancestors of one node and checking from other's traversal, you do a set intersection everytime

# Queues -- VIMP
# Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.
# Reference: https://medium.com/@shuangzizuobh2/how-well-do-you-code-python-9bec36bbc322
# Reference: https://docs.python.org/2/library/collections.html#collections.deque 
from collections import deque
deque(['f', 'g', 'h', 'i', 'j'])
access = deque([])  # initializing queues
d.pop()         # 'j'   O(1)
d.popleft()     # 'f'   O(1)
d.append('s')   # add in end
a.insert(3, '4')    # add at sepcific index
# Note: Both are O(1) because these are built on top of linked list implementations (pointers to both ends) along with array concepts of contiguous memory for quick retrieval -- A very high level understanding
# Note: Both stacks / lists and queues support peek() operation which just looks at the top or last element respectively without removing it

# reverse list iteration
a = ['a', 'b', 'c']
for item in reversed(a):
    print(item)    # ['c', 'b', 'a']

# for in with reversed index
for i in reversed(range(5)):
    print(i)    # 4,3,2,1,0

# for with step
for i in range(10, 4, -2):  # start, stop, step :: until [element > stop]
    print(i)    # 10,8,6 

# set
s = {1, 3, 4}
s2 = {4, 5, 7}
s.update(s2)  # {1, 3, 4, 5, 7}

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

# IMP: string concatenation takes O(n) time! Therefore if concatentaion is a major part of your algo, use array append and then "".join(array) to get resultant string which will have amortized O(1) time
# i.e. Instead of `str +=`, use res_array & then ``"".join(res_array)` approach coz str+ takes O(n) time every time you add a character due to the underlying implementation (read more)


# For int array, use:
ch = ''
for i in a:
    ch += i
# o: 'abcd'
''.join([str(elem) for elem in a])     # when a has int elements

# sort a string and return string
q = "qssi"
"".join(sorted(q))  # 'iqss'
sorted(q)           # returns --> ['i', 'q', 's', 's'] but doesn't change q --- # REMEMBER: q doesn't change when you use "sorted"

# ------------------------------------------------------------------ #


# dictionaries
d = {"aa": 3, "bb": 4, "cc": 2, "dd": [1, 3]}
list(d.keys())      # returns all keys as a list
list(d.values())    # returns all values in the dict as a list
# access keys in sorted fashion
for a in sorted(d.keys()):
  print(a)

# get "key" value or return "default" if key doesn't exist
dict.get("key", "default") 

# similar to get but also sets the default in dictionary along with returning it
dict.setdefault("key", [])     

# remove and return if "key" exists. 
del dict["key"]
# or: if not return "default"
dict.pop("key", "default")  

# sort dictionary in descending order and return a list
d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

# setting tuple as dict key. Note: Only Immutable objects can be set as keys. Therefore list directly cannot be a key to a dict. Tuple can be
# https://stackoverflow.com/questions/7027199/hashing-arrays-in-python
a[tuple([4,5,6])] = 5   # can directly use tuple for key. list -> tuple just for demo purposes 
a[(4,5,6)]              # returns 5
# frozenset: immutable form of a set

# tuples
# remember that single values tuples are created like: (5,) and not simply (5) bcz of paranthesis and syntax related issues

# List values in dictionary are references: if you mutate an array stored in a dictionary after storing it, the value stored in doctionary also changes!
d = {}
arr = [3, 5, 6] 
d[1] = arr
arr.append(7)
d[1] # [3,5,6,7] even though you did not change the dictionary value, the reference is the same!
# use tuples for non-mutation

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

# lambda -- Anonymous functions assigned to variables
x = lambda a, b: a * b
print(x(5, 6))      # 30

# Remember: map & filter always return map & filter objects -- pass them in list() to get lists
# map
# map(fun, iter)
def addition(n): 
    return n + n 
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)      # [2, 4, 6, 8]

# filter - 1: Based on filter function
# https://www.programiz.com/python-programming/methods/built-in/filter
nums = [-1, 3, 0, -3, 4, 4, -29]
filteredNums = filter(lambda a : a>0, nums) # can also use a proper function in place of lambda
print(list(filteredNums)) # [3, 4, 4]

# filter - 2: Based on None: returns every legit value: skips False, None, 0
nums = [-1, 3, 0, False, None, 4, -29, 'a', 'false']
filteredNums = filter(None, nums)
list(filteredNums)  # [-1, 3, 4, -29, 'a', 'false']

# date
import datetime
datetime.datetime.strptime('15:30','%H:%M') # change string to time
datetime.datetime.now()     # get current time
# also time objects can be compared directly

# Dynamic Arrays: amortized analysis
# TLDR;
# Insertion at end: Amortized O(1)
# Insertion at middle or end: O(N)
#
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

# enums
# TODO: Add more resources
# https://www.tutorialspoint.com/enum-in-python

# tuple assignment
r,c = 2, 4 or r,c = (2, 4) # both work
c   # 4
(r,c) == (2,4)             # True
# when returning or checking, need to use tuple

# ---- Lists Extended Concepts
# sort characters in a string + example of map and lambda
words = ["yace", "cea", "aeca"]
sorted_chars = list(map(lambda word: ''.join(sorted(word)), words))
# ['acey', 'ace', 'aace']

# Sorting a string can even be O(N) by counting sort as you know the toal number of characters in ASCII: 127
# https://stackoverflow.com/questions/4433915/why-is-sorting-a-string-on-log-n#:~:text=O(n%20log%20n)%20is,choose%20to%20solve%20this%20task.

# sorting a list based on another list eg here: indices sorted based on strings in a different list (of course the strings and the indices are complementary) 
words = ["race", "blink", "oy", "yo", "linkb", "care"]
sorted_words = list(map(lambda word: ''.join(sorted(word)), words))   # ['acer', 'bikln', 'oy', 'oy', 'bikln', 'acer']
# sorted_words = ["".join(sorted(w)) for w in words]        # another way of creating list after sorting characters of every string
indices = [i for i in range(len(words))]
indices.sort(key=lambda x: sorted_words[x])
indices
# [0, 5, 1, 4, 2, 3]    # which represents the indices of words if they were sorted in sorted_words - leading to grouping of anagrams

# Understanding Array Assignment & copy
# Array assignment in a temp variable is a shallow copy. it is just a copy of reference
# var assignment = O(1) time & space
# deep copy using copy = O(n) time & O(n) space
l = [1, 45, 7]
id(l)
m = l                   # reference copy or shallow copy
n = l.copy()            # deep copy
print(id(l)==id(m))     # True
print(id(l)==id(n))     # False



