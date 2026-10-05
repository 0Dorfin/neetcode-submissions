class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        longest = 0
        set_strings = set()

        for R in range(len(s)):
            while s[R] in set_strings:
                set_strings.remove(s[L])
                L += 1
            window = (R - L) + 1
            longest = max(longest, window)

            set_strings.add(s[R])
        return longest
