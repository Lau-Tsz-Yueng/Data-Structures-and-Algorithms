## 1481.
## 给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目

##示例 输入：arr = [5,5,4], k = 1
##输出：1
##解释：移除 1 个 4 ，数组中只剩下 5 一种整数。

##输入：arr = [4,3,1,1,3,3,2], k = 3
##输出：2
##解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。

## 自己的做法:

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        vote = {}
        for j in range(len(arr)):
            if arr[j] not in vote:
                vote[arr[j]] = 1
            elif arr[j] in vote:
                vote[arr[j]] += 1     ## 这里主要是将arr放入哈希表中
        ans = list(vote.values())     ## 将vote字典中的value值 数组化，
        ans.sort()                    ## 再将数组排序
        for i in range(k):
            if ans[0] > 1:
                ans[0] -= 1
            elif ans[0] == 1:
                ans.pop(0)
        return len(ans)
        
## 别人的优秀做法 值得学习 使用collections库中的自带的Counter去实现
## 计数器

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        import collections
        count_list = collections.Counter(arr)
        sort_val = sorted(count_list.values())
        for index,val in enumerate(sort_val):
            if(k>=val):
                k = k- val
            else:
                return len(sort_val) - index
        return 0
