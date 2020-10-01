# Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

# If there is no common subsequence, return 0.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.

# ---------------------------------------------------SOLUION------------------------------------------------------------

# PYTHON
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        ar=[[0]*(m+1) for z in range (n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    ar[i+1][j+1]=ar[i][j]+1
                else:
                    ar[i+1][j+1]=max(ar[i][j+1],ar[i+1][j])
        return ar[-1][-1]
