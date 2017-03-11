# coding: utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 用哈希表存储，查找效率高
        lookup = {}

        # 遍历 nums
        for i, num in enumerate(nums):

            # 若它的另一半就在 lookup 中，则可以返回结果了
            if target - num in lookup:
                return [lookup[target - num], i]
            
            # 若曾经未见过它的另一半，先将它本身存下来
            lookup[num] = i

# 试调用
s = Solution()
nums = [1, 3, 5, 9]

print s.twoSum(nums, 10)