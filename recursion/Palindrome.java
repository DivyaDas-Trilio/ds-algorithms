public class Palindrome {
    public static String l_str = "";
    public static String r_str = "";
    public void str_match(String s, int i, int n){
        if(i == n) return;
        l_str += s.charAt(i);
        str_match(s, i+1, n);
        r_str += s.charAt(i);
        
        if(l_str.equals(r_str)) System.out.println("Palindrome.");

    }
    public static void main(String[] args) {
        Palindrome p = new Palindrome();
        String s = "123432";
        int n = s.length();
        p.str_match(s, 0, n);
    }
}
