class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        count = len(seen)

        if count == 26:
            return True 
        else:
            return False 



        