class solution:
    dict = {}
    def ladderLength(self, beginWord, endWord, wordList):
        self.createDictionary(wordList)
        access = [beginWord]
        count = 0
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
            temp = word
            temp[i] = '*'
            pattern.append(temp)
        return pattern
