# --- Auxiliary indices array sorted based on a target array
target_arr = [34, 6, 7, 0, 2, 12, 10]
indices = [i for i in range(len(arr))]
indices.sort(key=lambda x: arr[x])    # [3, 4, 1, 2, 6, 5, 0]

# --- File to store util functions which can be useful

# takes in an sorted array in descending order & a target, returns the first number from left which is smaller or equal to the target. If no number is smaller than the given number, return None
# Approach: Modified Binary search
# Complexity: O(log n) where n is the length of the array
# Pre requisite: for complexity to be O(log n) and this function to be useful, array should be already sorted

# Note: passed array is in descending order
# Note: that to return for an unsorted array, do a single pass and return in O(n) time. This is useful only when the array is already sorted
def largestPossibleDivisor(array, target):
  length = len(array)
  lo = 0
  hi = length - 1
  largestPossibleDivisor = None
  while lo <= hi:
    mid = int((lo+hi)/2)
    if target == array[mid]:
      return array[mid]
    elif target > array[mid]:
      # go left as array is sorted in descending order
      # whenever you find target > array[mid] (i.e whenever you go left) update largestPossibleDivisor
      largestPossibleDivisor = array[mid]
      hi = mid -1
    else:
      # keep going right as array is sorted in descending order
      lo = mid + 1
  return largestPossibleDivisor


largestPossibleDivisor([17,13,9,7,5,2,1,0], 4)      # 2
largestPossibleDivisor([17,13,9,7,5,2,1,0], 99)     # 17
largestPossibleDivisor([17,13,9,7,5,2,1,0], 2)      # 2
largestPossibleDivisor([17,13,9,7,5,2,1,0], 12)     # 9

# ---------------------------------------------------------------------



