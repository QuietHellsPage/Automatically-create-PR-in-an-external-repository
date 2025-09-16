"""
ALL THE SOLUTIONS TO THE PROBLEMS
"""

"""
LEVEL 1 - EASY LEVEL
"""


"""
1. Two sum
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        match = {}
        for i, v in enumerate(nums):
            rem = target - v
            if rem in match:
                return [match[rem], i]
            match[v] = i
        return []


"""
2. Palindrome number
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]


"""
3. Longest common prefix
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                pref += i[0]
            else:
                break
        return pref


"""
4. Valid parentheses
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in s:
            if i in mapping:
                el = stack.pop() if stack else "#"
                if mapping[i] != el:
                    return False
            else:
                stack.append(i)
        return not stack


"""
5. Remove duplicates from sorted array
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[f-1]:
                nums[f] = nums[j]
                f += 1
        return f


"""
6. Remove element
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


"""
7. Find the index of the first occurrence in a string
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


"""
LEVEL 2 - MEDIUM
"""


"""
1. Longest palindromic substring
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s:
            return ""
        
        
"testing string"
"test"
"test"