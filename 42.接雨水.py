#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30404
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (66.07%)
# Likes:    6398
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 2.9M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]\n[4,2,0,3,2,5]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        e.g. 如果 height = [3, 0, 2, 0, 4]
        那么对于位置 1, 左边最高是3, 我一直加水, 一直加水, 加到2之后, 这个水回流过位置 2,
        穿到位置 3, 然后位置 3 会一直加水, 加到高度 2 之后, 中间的一排就可以以此加水了, 最高只能到 3,
        因为位置 0 挡住了

        对于任意位置 i, 只需要知道3个数字就可以算出高度:
        左边最高柱子高度 left_max
        右边最高柱子高度 right_max
        当前的柱子高度 height[i]

        水位 = min(left_max, right_max)
        水量 = 水位 - height[i]
        """
        # 从左往右找左侧高的位置
        n = len(height)
        left_max = [0] * n
        left_max[0] = height[0]
        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        res = 0
        for i in range(n):
            res = res + min(left_max[i], right_max[i]) - height[i]

        return res


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
