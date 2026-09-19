from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        required = len(need)

        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:

                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]