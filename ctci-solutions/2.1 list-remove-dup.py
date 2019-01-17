# Reference: CTCI. Pg 50
# Author: Shreyas Padhye

# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from util.linked_list_util import linked_list

class list_remove_dup():
    def __init__(self, Arr):
        self.input_list = linked_list()
        for item in Arr:
            self.input_list.append(item)
    
    def remove_dup(self):
        return self.input_list.display()

mylist = list_remove_dup([3, 5, 6, 3, 1, 3])
mylist.remove_dup()

