class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                nums[slow] = nums[fast]
                slow +=1
        return slow +1
        