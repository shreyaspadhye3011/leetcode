class solution:
    def run_length_encoding(self, s):
        curr_ele = ""
        curr_count = 0
        result = ""
        for char in s:
            if char == curr_ele:
                curr_count += 1
            else:
                result += curr_ele
                if curr_count > 1:
                    result += str(curr_count)
                curr_ele = char
                curr_count = 1
        
        # to append last element -- becaus it will never make it to result as it will always match itself
        result += curr_ele
        if curr_count > 1:
            result += str(curr_count)
        return result
    
t = solution()
# t.run_length_encoding("aaabbb")
# t.run_length_encoding("aaabbbc")
# t.run_length_encoding("abcc")
# t.run_length_encoding("abc")
t.run_length_encoding("aaa")
t.run_length_encoding("aab")
t.run_length_encoding("aba")
t.run_length_encoding("abb")
t.run_length_encoding("abbaaa")
                
            