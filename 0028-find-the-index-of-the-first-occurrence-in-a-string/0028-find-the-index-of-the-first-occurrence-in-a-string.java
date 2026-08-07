class Solution {
    public int strStr(String haystack, String needle) {

        for (int i = 0; i <= haystack.length() - needle.length(); i++) {

            if (haystack.charAt(i) == needle.charAt(0)) {

                int index = 0;
                String s = "";
                int x = i;

                for (int j = i; j < i + needle.length(); j++) {

                    if (haystack.charAt(j) == needle.charAt(index)) {
                        s += haystack.charAt(j);
                        index++;
                    } else {
                        break;
                    }
                }

                if (s.equals(needle)) {
                    return x;
                }
            }
        }

        return -1;
    }
}