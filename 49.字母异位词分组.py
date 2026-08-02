#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30404
#
# [49] 字母异位词分组
#
# https://leetcode.cn/problems/group-anagrams/description/
#
# algorithms
# Medium (69.46%)
# Likes:    2761
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 2.4M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]\n[""]\n["a"]'
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
#
#
# 示例 1:
#
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 解释：
#
#
# 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
# 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
#
#
#
# 示例 2:
#
#
# 输入: strs = [""]
#
# 输出: [[""]]
#
#
# 示例 3:
#
#
# 输入: strs = ["a"]
#
# 输出: [["a"]]
#
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母
#
#
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. 个str -> List[str]
        2. 然后把List[str]拼接在一起
        """
        strs_dict: dict[str, List[str]] = defaultdict(list)
        for _str in strs:
            strs_dict["".join(sorted(_str))].append(_str)
        return list(strs_dict.values())


# @lc code=end


#
# @lcpr case=start
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#
