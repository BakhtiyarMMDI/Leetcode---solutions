class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = " ".join(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]  
        return list(groups.values())      