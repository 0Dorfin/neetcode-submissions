class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        longest = ""
        longest_len = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                len_pal = right - left + 1
                if len_pal > longest_len:
                    longest_len = len_pal
                    longest = s[left:right + 1]
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                len_pal = right - left + 1
                if len_pal > longest_len:
                    longest_len = len_pal
                    longest = s[left:right + 1]
                left -= 1
                right += 1

        return longest
                    
