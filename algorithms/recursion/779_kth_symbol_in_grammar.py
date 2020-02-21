# Reference: https://leetcode.com/problems/k-th-symbol-in-grammar/
# Approach: Notice the pattern: 
# For row m, when m is even, pattern(m-1) is taken & !(pattern(m-1)) is appended to get value of row m
# when m is odd, pattern(m-1) is taken & rev(pattern(m-1)) is appended to get value of row m