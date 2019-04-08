# min knight move -- https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/
# valid binary search tree -- https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

# whole minute dilemma -- given an array, find max possible pairs

# TLE in few cases
def wholeMinute(songs):
    count = 0
    songs = list(map(lambda x: x%60, songs))
    for i in range(0, len(songs)):
        if songs[i] == 0:
            count += songs[i+1:].count(0)
        else:
            count += songs[i+1:].count(60 - songs[i])
    return count
    
# wholeMinute([30, 60, 114])
# wholeMinute([4, 10, 50, 90, 30])
wholeMinute([3, 60, 60, 60])