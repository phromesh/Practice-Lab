# longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[i])
            max_len = max(max_len, i-start+1)
        return max_len
    
sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))