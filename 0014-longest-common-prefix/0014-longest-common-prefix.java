class Solution {
    public String longestCommonPrefix(String[] strs) {
     Arrays.sort(strs);
     String s = strs[0];
     String ans ="";
     String s1 = strs[strs.length-1];
     for(int i=0;i<Math.min(s.length(),s1.length());i++){
        if(s.charAt(i)==s1.charAt(i)){
            ans+=s.charAt(i);
        }else{
            break;
        }
     }
return ans.toString();
    }
}