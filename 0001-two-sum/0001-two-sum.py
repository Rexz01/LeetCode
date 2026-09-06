class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[]
        for i in range(len(nums)):
            x =i
            for j in range (i+1 ,len(nums)):
                y=j
                if nums[i]+nums[j]== target:
                    li.append(x)
                    li.append(y)
                    return li
        return li