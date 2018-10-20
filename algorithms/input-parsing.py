# Reference: https://codejam.withgoogle.com/codejam/resources/quickstart-guide#io-tutorial

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options

## File Reading: reads input format from `input_file.txt` and writes to `output_file.txt`
# python3 input-parsing.py < input_file.txt > output_file.txt
 
 