#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30404
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (54.59%)
# Likes:    2020
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.1M
# Testcase Example:  '"cbaebabacd"\n"abc"\n"abab"\n"ab"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
#
#
# 示例 1:
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
#
# 示例 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
#
#
# 提示:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
#
#
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """用固定长度窗口查找所有字母异位词。"""
        sLength = len(s)
        pLength = len(p)

        if pLength > sLength:
            return []

        targetCount = Counter(p)
        windowCount = Counter(s[:pLength])
        result = []

        # 检查第一个窗口
        if windowCount == targetCount:
            result.append(0)

        for right in range(pLength, sLength):
            # 移除旧窗口最左侧的字符
            leavingChar = s[right - pLength]
            windowCount[leavingChar] -= 1
            if windowCount[leavingChar] == 0:
                del windowCount[leavingChar]

            # 加入新窗口最右侧的字符
            windowCount[s[right]] += 1

            if windowCount == targetCount:
                result.append(right - pLength + 1)

        return result


# @lc code=end


#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#
