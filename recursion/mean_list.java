class MeanList{

    public double mean_list(double[] lst, int i, int n){

        if(i==n) return lst[i];
        return lst[i] + mean_list(lst, i+1, n);

    }
    public static void main(String[] args){
        MeanList obj = new MeanList();
        double[] lst = {1,2,3,4,5};
        System.out.println(obj.mean_list(lst, 0, 4)/lst.length);
    }
    
}
