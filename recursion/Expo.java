public class Expo {

    public static int expoCalculate(int a, int b){
        if(b==1) return a;

        return a * expoCalculate(a, b-1);
    }
    public static void main(String[] args) {
        System.out.println(Expo.expoCalculate(2,10));
    }
    
}
