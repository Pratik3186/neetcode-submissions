class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen  = {}

        for i in range(len(nums)):
            complementry = target - nums[i]
            if complementry in seen:
                return [seen[complementry],i]
            seen[nums[i]] = i
            
        


        