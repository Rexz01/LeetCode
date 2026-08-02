class Solution {
    public int lengthOfLastWord(String s) {
    
        int n  = s.length()-1;
        String x =" ";
        int count =0 ;
        for(int i = n ;i>=0;i--){
            if(s.charAt(i)!=' '){
              count++;
            }else if (s.charAt(i) ==' ' && count!=0){
                break;
            }
        }
        return count;
    }
}