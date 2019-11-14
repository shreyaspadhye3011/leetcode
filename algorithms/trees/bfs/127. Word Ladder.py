# Reference: https://leetcode.com/problems/word-ladder/

# Approach 1: Create dictionary that stores all possible one letter variations from the wordlist given. Keep checking whether the endWord's variation have arrived in the dictionary. If yes, then return count of how many steps it took. If the whole list is complete and you do not reach any return point means that there is no solution

# Issue: The solution assumes connected graph. But there's no such restriction. What if log -> cog is a possible transition by "log" being one of the words and "cog" being the end word but there is no link between "Hit" the beginWord and "log" to finally reaching "cog". So the assumption of it being a connecgted graph doesn't fit the problem. Also the solution assumes the given wordList to grow in a transformative fashion to give out the count correctly. It's possible that "log" might be encountered as the first word in the list and would give out result as 1 but that's wrong.

############

# Approach 2: Create a dictionary that stores all possible one letter variations from the wordlist given. Do a BFS like algo. For every word from the access list, get all words from it's "one word varitaion" dictionary key and put them in access list. Return count when endWord is found in access list
class solution:
    dict = {}
    def ladderLength(self, beginWord, endWord, wordList):
        self.createDictionary(wordList)
        access = [beginWord]
        count = 1    # because solution considers length of the path so that includes beginWord also
        accessed = []
        while len(access) != 0:
            currWord = access.pop()
            if currWord == endWord:
                return count
            count += 1
            accessed.append(currWord)
            for iword in self.getRegEx(currWord):
                for rword in self.dict.setdefault(iword, []):
                    if rword not in accessed:
                        access.append(rword)
        return 0
    
    def createDictionary(self, wordList):
        for word in wordList:
            for iword in self.getRegEx(word):
                self.dict.setdefault(iword, []).append(word)

    def getRegEx(self, word):
        pattern = []
        for i in range(len(word)):
            temp = word[:i] + '*' + word[i+1:]
            pattern.append(temp)
        return pattern

obj = solution()
obj.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])   # o: 5
# obj.dict
