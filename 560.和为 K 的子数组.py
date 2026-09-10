#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30404
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (46.77%)
# Likes:    3245
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '[1,1,1]\n2\n[1,2,3]\n3'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
#
#
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # 前缀为0的prefix count 初始为 1
        total = 0
        ans = 0

        for num in nums:
            total += num  # 目前总和为 total
            ans += prefix_count.get(
                total - k, 0
            )  # 看看前缀和多少个total - k, 如果没有就是 0
            # 为什么呢: 因为现在你的总和为total, 如果前缀为 total - k, 那么你把前缀删掉, 那这个子数组就是 k
            prefix_count[total] += 1  # 总和为 total 的前缀和
        return ans


# @lc code=end


#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#
