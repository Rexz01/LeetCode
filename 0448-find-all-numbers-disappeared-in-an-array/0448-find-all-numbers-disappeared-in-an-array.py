class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans=[]
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
     
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans