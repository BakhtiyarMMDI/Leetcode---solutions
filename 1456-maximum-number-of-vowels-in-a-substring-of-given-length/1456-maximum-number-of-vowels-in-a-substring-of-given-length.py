class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        max_vowels = 0
        window_vowels = 0
        # count vowels in the frist window
        for i in range(k):
            if s[i] in vowels:
                window_vowels += 1
        max_vowels = window_vowels

        #slide the window 
        for i in range(k, len(s)):
            # remove the left character
            if s[i - k] in vowels:
                window_vowels -= 1
            # add the new right character 
            if s[i] in vowels:
                window_vowels += 1
            
            max_vowels = max(max_vowels, window_vowels)
        return max_vowels


        