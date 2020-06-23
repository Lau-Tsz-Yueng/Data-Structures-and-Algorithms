##78 Leetcode

##给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

##说明：解集不能包含重复的子集。

## 输入: nums = [1,2,3]
## 输出:[
##  [3],
##  [1],
##  [2],
##  [1,2,3],
##  [1,3],
##  [2,3],
##  [1,2],
##  []]

##mine:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def backtrack(First=0, tmp=[]):
            tmp.sort()
            for j in range(len(tmp)):
                if tmp.count(tmp[j]) > 1:
                    break
                if j == len(tmp)-1 and tmp not in ans:
                    ans.append(tmp)
            for i in range(First, len(nums)):
                if nums[First] not in tmp:
                    backtrack(First + 1, tmp+[nums[i]])
        backtrack()
        return ans
        
##优化解 或者说 巧解 本身没有运用回溯思想：
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for n in nums:
            for i in range(len(ans)):
                ans.append(ans[i]+[n])
        return ans
