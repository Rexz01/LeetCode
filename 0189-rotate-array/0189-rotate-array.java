class Solution {
    public void rotate(int[] nums, int k) {
        int ans []=  new int [nums.length] ;
        k = k%nums.length;
        int x = nums.length-k;
        int index=0;
        for(int i =x;i<nums.length;i++){
            ans[index++]= nums[i];
        }
        for(int i =0 ;i<x;i++){
            ans[index]=nums[i];
            if(index<ans.length){
                index++;
            }
        }
        for(int i =0 ;i<ans.length;i++){
            nums[i]=ans[i];
        }
    }
}