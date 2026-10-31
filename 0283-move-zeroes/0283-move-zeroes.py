class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li=[]
        le=[]
        for i in range(len(nums)):
            if nums[i]==0:
                li.append(nums[i])
            else:
                le.append(nums[i])
        
        for i in range(len(le)):
            nums[i]=le[i]
        x=len(le)
        for i in range(len(li)):
            nums[x]=li[i]
            x+=1
        return nums