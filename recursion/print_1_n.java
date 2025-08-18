class Print1ToN{

    public void print(int num){
        if(num == 0) return;
        print(num-1);
        System.out.println(num);
    }
    public static void main(String[] args){
        Print1ToN obj = new Print1ToN();
        obj.print(10);
    }
}