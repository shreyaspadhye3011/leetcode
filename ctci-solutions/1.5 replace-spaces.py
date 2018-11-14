# Problem (pg 100): Write a method to replace all spaces in a string with ‘%20’

class solution():
    def replace_spaces(self, s):
        res = ""
        for char in s:
            if char == ' ':
                res += '20%'
            else:
                res += char
        return res
    
t = solution()
t.replace_spaces("a b")
t.replace_spaces("abc ")
t.replace_spaces("abc")
t.replace_spaces("  abc")
t.replace_spaces("a b c")
t.replace_spaces("   ")
t.replace_spaces("20%")
t.replace_spaces("20%a")
t.replace_spaces("2x10%20%")

