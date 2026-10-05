class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0
        longest = 0
        set_strings = set()

        while R < len(s):
            if s[R] not in set_strings:
                set_strings.add(s[R])
                window = (R - L) + 1
                longest = max(longest, window)
                R += 1
            else:
                set_strings.remove(s[L])
                L += 1
        
        return longest
        