#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30404
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (48.80%)
# Likes:    2937
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 3.4M
# Testcase Example:  '[100,4,200,1,3,2]\n[0,3,7,2,5,8,4,6,0,1]\n[1,0,1,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
# 示例 3：
#
# 输入：nums = [1,0,1,2]
# 输出：3
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            # 如果 nums 为空
            return 0
        nums = set(nums)  # 把 nums 变成哈希集合, 搜索复杂度为 O(1)
        max_len = 0
        for num in nums:
            if num - 1 in nums:
                # 先找到一个序列的开头,如果不是开头就找到开头
                continue
            else:  # 前一个数字已经不在nums中了, 从当前的 num 开始往后找
                cur_num = num
                cur_len = 0
                # 从现在开始往后一直加 1
                while cur_num in nums:
                    cur_num += 1
                    cur_len += 1
                max_len = max(cur_len, max_len)
        return max_len


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#
