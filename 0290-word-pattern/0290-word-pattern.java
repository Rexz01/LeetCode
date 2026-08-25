class Solution {
    public boolean wordPattern(String pattern, String s) {

        Map<Character ,String> map = new HashMap<>();
          Map<String, Character> map1= new HashMap<>();
          String[] arr = s.split(" ");
            if (pattern.length() != arr.length) {
            return false;
        }
        for (int i =0 ;i<pattern.length();i++){
          char c1 = pattern.charAt(i);
          String r = arr[i];

            if (map.containsKey(c1)) {
                if (!map.get(c1).equals(r)) {
                    return false;
                }
            } else {
                map.put(c1,r);
            }

            if (map1.containsKey(r)) {
                if (map1.get(r)!=c1) {
                    return false;
                }
            } else {
                map1.put(r, c1);
            }
        }

        return true;

        } 
    }
