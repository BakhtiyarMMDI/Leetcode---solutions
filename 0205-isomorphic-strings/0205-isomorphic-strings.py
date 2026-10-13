class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}

        for i in range (len(s)):
            if s[i] in seen:
                if seen[s[i]] != t[i]:
                    return False
            else:
                if t[i] in seen.values():
                    return False
                seen[s[i]] = t[i]
        
        return True 
        