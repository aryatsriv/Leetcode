#3. Longest Substring Without Repeating Characters
#Solved
#Medium
#Topics
#Companies
#Hint
#Given a string s, find the length of the longest 
#substring
# without repeating characters.
#
# 
#
#Example 1:
#
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:
#
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
#
#Constraints:
#
#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        n=len(s)
        maxCount=0
        cache={}

        while j<n:
            while s[j] in cache:
                cache[s[i]]-=1
                if cache[s[i]]==0:
                    cache.pop(s[i])
                i+=1
            cache[s[j]]=1
            maxCount=max(j-i+1,maxCount)
            j+=1

        return maxCount



            
