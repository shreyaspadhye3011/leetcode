# Reference: CTCI. Pg 48
# Author: Shreyas Padhye

# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).

# Algorithm: Add first string to itself and check a) s2 is a substring of the added s1 string  

class solution():
    def check_string_rotation(self, s1, s2):
        if len(s1) == len(s2):
            s1 += s1
            if s1.find(s2) > -1:
                # not needed: checking whether remainder is the same string -- was an extra check which I initially added but then removed as length check handles that case
                # s1 = s1[:i] + s1[i+original_len:]
                # print(s1)
                # if s1 == original_str:
                #     return True
                return True
        return False

obj = solution()
obj.check_string_rotation("waterbottle", "erbottlewat")    # True
obj.check_string_rotation("waterbottle", "rbottlewat")     # False
obj.check_string_rotation("abc", "bca")     # True
obj.check_string_rotation("aabc", "aabc")     # True
obj.check_string_rotation("abAc", "abac")     # False
obj.check_string_rotation("abac", "aabc")     # False
obj.check_string_rotation("kklmo", "klmo")     # False
obj.check_string_rotation("kkkk", "kkkk")     # True
obj.check_string_rotation("akkb", "bakk")     # True
obj.check_string_rotation("a", "aa")     # False