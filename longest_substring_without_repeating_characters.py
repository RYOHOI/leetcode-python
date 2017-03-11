# coding: utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        break_point = 0
        max_length = 0
        for i, letter in enumerate(s):

            # 这个字母在当前子串中（因此要检验 letter 位置大于 break_point）
            if letter in lookup and lookup[letter] >= break_point:

                # 断点往前挪到当前字母在子字符串中位置的下一个
                break_point = lookup[letter] + 1

            # 从已有的最大值、及当前子字符串长度中，得到新的最大值
            max_length = max(max_length, i - break_point + 1)
            
            lookup[letter] = i

        return max_length

s = Solution()
print s.lengthOfLongestSubstring('laststringest')
# output: 7
# "stringe"