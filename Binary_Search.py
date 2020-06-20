## 81
## Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
##(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
##You are given a target value to search. If found in the array return true, otherwise return false.


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] <= target:
                l = mid + 1
        return False

##Classic Binary Search, O(log(n)) complexity, 经典二分查找。
