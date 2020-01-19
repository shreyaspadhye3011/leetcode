# for in reversed
for i in reversed(range(5)):
    print(i)    # 4,3,2,1,0

# for with step
for i in range(10, 4, -2):  # start, stop, step :: until [element > stop]
    print(i)    # 10,8,6   

# list comprehension

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

# lists
a = ['a', 'b', 'c', 'd']    # implode lists or join
''.join(a)
# o: 'abcd'

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