#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30404
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (40.55%)
# Likes:    8149
# Dislikes: 0
# Total Accepted:    3.1M
# Total Submissions: 7.5M
# Testcase Example:  '[-1,0,1,2,-1,-4]\n[0,1,1]\n[0,0,0]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
#
# 示例 2：
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#
# 示例 3：
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # n 为 3，从 nums[0] 开始计算和为 0 的三元组
        return self.nSumTarget(nums, 3, 0, 0)

    # 注意：调用这个函数之前一定要先给 nums 排序
    # n 填写想求的是几数之和，start 从哪个索引开始计算（一般填 0），target 填想凑出的目标和
    def nSumTarget(
        self, nums: List[int], n: int, start: int, target: int
    ) -> List[List[int]]:
        size = len(nums)
        res = []
        # 至少是 2Sum，且数组大小不应该小于 n
        if n < 2 or size < n:
            return res
        # 2Sum 是 base case
        if n == 2:
            # 双指针那一套操作
            low, high = start, size - 1
            while low < high:
                sum_val = nums[low] + nums[high]
                left, right = nums[low], nums[high]
                if sum_val < target:
                    while low < high and nums[low] == left:
                        low += 1
                elif sum_val > target:
                    while low < high and nums[high] == right:
                        high -= 1
                else:
                    res.append([left, right])
                    while low < high and nums[low] == left:
                        low += 1
                    while low < high and nums[high] == right:
                        high -= 1
        else:
            # n > 2 时，递归计算 (n-1)Sum 的结果
            for i in range(start, size):
                # Skip the duplicate element to avoid duplicate triplet
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    # (n-1)Sum 加上 nums[i] 就是 nSum
                    arr.append(nums[i])
                    res.append(arr)
        return res


# @lc code=end


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#
