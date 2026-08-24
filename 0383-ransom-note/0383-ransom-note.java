class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> m = new HashMap<>();
        for(int i =0;i<magazine.length();i++){
            m.put(magazine.charAt(i),m.getOrDefault(magazine.charAt(i),0)+1);
        }
        for (char ch : ransomNote.toCharArray()) {
    if (m.getOrDefault(ch, 0) == 0) {
        return false;
    }
    m.put(ch, m.get(ch) - 1);
}
return true;
    }
}