class StringReverse{
    public void reverse(String s, int i, int n){
        if(i == n) return;
        reverse(s, i+1, n);
        System.out.print(s.charAt(i));

    }
    public static void main(String[] args) {
        StringReverse sr = new StringReverse();
        String s = "Divya Jyoti Das";
        int n = s.length();
        sr.reverse(s, 0, n);
    }
}