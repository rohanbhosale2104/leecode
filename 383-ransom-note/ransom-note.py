from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq=Counter(magazine)
        for ch in ransomNote:
            if freq[ch]==0:
                return False
            freq[ch]-=1
        return True
        # if ransomNote in magazine or ransomNote in magazine[::-1]:
        #     return True
        # return False