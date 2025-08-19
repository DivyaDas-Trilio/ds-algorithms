class PrintBinary {

    public int printBinToDecimal(String bin){
        StringBuilder sb = new StringBuilder(bin);
        sb.reverse();
        int sum = 0;
        for (int i = 0; i < sb.length(); i++) {
            if(sb.charAt(i) == '1')
                sum += Math.pow(2, i);
        }
        return sum;

    }

    public void printBinary(int num, String osf){
        PrintBinary pb = new PrintBinary();
        if(pb.printBinToDecimal(osf) > num) return; 
        if(pb.printBinToDecimal(osf) == num) System.out.println(osf);

        printBinary(num, osf+"0");
        printBinary(num, osf+"1");
    }
    public static void main(String[] args) {
        PrintBinary pb = new PrintBinary();
        // System.out.println(pb.printBinToDecimal("111"));
        for(int i=0; i<=32;i++)
            pb.printBinary(i, "1");
    }
}
