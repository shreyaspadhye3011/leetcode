# Reference: CTCI. Pg 50
# Author: Shreyas Padhye

# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from util.linked_list_lib import linked_list

### Buffer allowed
# Algorithm 1: keep a secondary buffer that keeps value of already iterated elements and while iterating keep checking this

### No buffer allowed
# Algorithm 2.A (more optimized, conceptually but **not appropriate** for linked lists as LL do not maintain indexing): as no extra buffer is allowed, we can sort the linked list and just check immediate neighbours (actually only left neighbour) to check duplicacy
# def remove_dup_nobuffer(self):

# Algorithm 2.B (appropriate for lists): for every element in list, look back and see all elements if already exist

class list_remove_dup():
    def __init__(self, Arr):
        self.input_list = linked_list()
        for item in Arr:
            self.input_list.append(item)
    
    def remove_dup(self):
        # print("JEE")
        # print(self.input_list.display())
        curr = self.input_list.head
        prev = curr
        iterated = []
        while curr.next != None:
            # VIMP - `curr = curr.next` has to be before the rest of the code if while condition is `curr.next != None` to iterate correctly so that both head and last element are correctly iterated
            curr = curr.next
            if curr.data in iterated:
                prev.next = curr.next
            else:
                iterated.append(curr.data)
        # print(self.input_list.display())
        return self.input_list

# mylist = list_remove_dup([3, 5, 6, 3, 1, 3])
# mylist = list_remove_dup([5, 5, 3, 5, 3])
mylist = list_remove_dup([5, 5, 5, 5, 5])
print(mylist)
# mylist = list_remove_dup([1, 2, 3, 5, 5])
# mylist.remove_dup()

