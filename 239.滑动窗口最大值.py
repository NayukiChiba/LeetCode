#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30404
#
# [239] 滑动窗口最大值
#
# https://leetcode.cn/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (50.29%)
# Likes:    3566
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3\n[1]\n1'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回 滑动窗口中的最大值 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#

# @lc code=start
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        # 先获取第一个最大值的 value 和 index
        if n == k:
            return [max(nums)]

        max_value = float("-inf")
        # 倒计时, 就是windows中的元素要滚出去的时间倒计时
        countdown = 0
        for i in range(n - k + 1):
            # 如果countdown到0了, 就可以重新计算windows的最大值和countdown了
            windows = nums[i : i + k]
            if countdown == 0:
                max_value = max(windows)
                countdown = k - windows[::-1].index(max_value)

            # 如果windows最后一个值 >= max value, 就要重新更新countdown了
            if windows[-1] >= max_value:
                max_value = windows[-1]
                countdown = k
            res.append(max_value)
            countdown -= 1
        return res


# @lc code=end


#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
