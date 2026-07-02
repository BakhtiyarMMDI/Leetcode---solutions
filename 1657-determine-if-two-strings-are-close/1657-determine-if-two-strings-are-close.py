class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False 

        count1 = {}
        count2 = {}

        for ch in word1:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1
        for ch in word2:
            if ch in count2:
                count2[ch] += 1
            else:
                count2[ch] = 1
        
        return sorted(count1.values()) == sorted(count2.values())

        