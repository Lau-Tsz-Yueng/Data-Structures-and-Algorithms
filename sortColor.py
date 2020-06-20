## Given an array with n objects colored red, white or blue, 
## sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
##
## Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
##
## Note: You are not suppose to use the library's sort function for this problem.
## Example:
## Input: [2,0,2,1,1,0]
## Output: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        r = len(nums) - 1
        cur = 0
        while cur <= r:
            if nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                cur += 1
                l += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            else:
                cur += 1
## QuickSorting algorithm, 类似与三指针快速排序，要注意的是 当交换2的时候 交换的这个元素是没有经过扫描的 所以使用cur的作用体现出来了

