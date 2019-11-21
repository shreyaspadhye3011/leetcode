# cut off minimum number of generators. model is an array of i where i is a type of generator. All generators of type i can be shut off at one go. At least Half of the generators need to be shut off
# status: all test cases working and expected
import math
def reduceCapacity(model):
    # create a count dictionary
    d = {}
    for item in model:
        value = d.get(item, 0)
        d[item] = value + 1
    
    # sort by count
    gen_type_count_map = [[k, d[k]] for k in sorted(d, key=d.get, reverse=True)]
#     print(gen_type_count_map)
    
    # calculate number of generators to be closed
    cutoff = math.ceil(float(len(model))/ 2)
    
    # get maximum from dictionary and keep removing until cutoff goal reached
    count = 0
    while cutoff > 0:
        [gen_type, gen_count] = gen_type_count_map.pop(0)
        cutoff -= gen_count
        count += 1
    
    return count

reduceCapacity([3,4,6,11,9,9,9,9,8,8,8,8,8,8])