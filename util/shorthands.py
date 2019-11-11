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