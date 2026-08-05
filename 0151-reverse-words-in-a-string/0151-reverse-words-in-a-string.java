class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        StringBuilder ans = new StringBuilder();
        int end = s.length();

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                if (i + 1 != end) {
                    ans.append(s.substring(i + 1, end)).append(" ");
                }
                while (i >= 0 && s.charAt(i) == ' ') {
                    i--;
                }
                end = i + 1;
            }
        }

        ans.append(s.substring(0, end));
        return ans.toString();
    }
}