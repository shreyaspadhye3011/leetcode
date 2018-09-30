
# coding: utf-8

# In[50]:


# https://leetcode.com/problems/add-two-numbers/description/
# Status: Solved using lists in python. This is not a linked list implementation
# Percentile: 

# Approach: Add index by index, keep a carry varaible that keeps updating. Also handle unmatched length of digits case
# Playground debugging: https://leetcode.com/playground/SSiaLgGs

# This code can't work with list inputs. This is only for ListNode inputs. Test on Leetcode playground if required
def addTwoNumbers(l1, l2):
    list1 = []
    list2 = []
    while l1:
        # print(l1.val)
        list1.append(l1.val)
        l1 = l1.next

    while l2:
        # print(l2.val)
        list2.append(l2.val)
        l2 = l2.next

    print(list1)
    print(list2)

    # get length of the lists to be used in for loop
    len1 = len(list1)
    len2 = len(list2)
    if (len1 > len2):
        length = len1
    else:
        length = len2
    carry = 0
    res = []
    for i in range(0, length):
        # case when both list still have numbers
        if (i < len1 and i < len2):
            if (list1[i] + list2[i] + carry <= 9):
                res.append(list1[i] + list2[i] + carry)
                # IMP: reinitialise carry to 0 when single digit result
                carry = 0
            else:
                res.append((list1[i] + list2[i] + carry) % 10)
                carry = (int((list1[i] + list2[i] + carry) / 10))
        # case when list2 is finishedd but list1 still has digits left
        elif (i < len1):
            if (list1[i] + carry <= 9):
                res.append(list1[i] + carry)
                carry = 0
            else:
                res.append((list1[i] + carry) % 10)
                carry = (int((list1[i] + carry) / 10))
        # case when list1 is finsihed but list2 still has digits [i.e when len2 > len1]
        else:
            if (list2[i] + carry <= 9):
                res.append(list2[i] + carry)
                carry = 0
            else:
                res.append((list2[i] + carry) % 10)
                carry = (int((list2[i] + carry) / 10))

    print(res)

# addTwoNumbers([2, 4, 3], [5, 6, 2w]) # A: 706 -> O: 6 -> 0 -> 7 
# addTwoNumbers([2, 4, 3], [5, 6]) # A: 407
# addTwoNumbers([2, 8, 9, 2], [8]) # A: 2990
# addTwoNumbers([9, 9, 9, 1], [1]) # A: 2000
# addTwoNumbers([0, 0, 8, 2], [0, 0, 2]) # A: 3000

