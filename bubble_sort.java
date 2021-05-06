public class BubbleSort{

    void bubble_sort(int mang[])
    {
        int phan_tu = mang.length;
        for (int i = 0; i < phan_tu-1; i++){
            for (int j = phan_tu-1; j > i; j--){
                if (mang[j] < mang[j-1])
                {
                    int temp = mang[j];
                    mang[j] = mang[j-1];
                    mang[j-1] = temp;
                }
            }
        }
    }
    
    public static void main(String args[])
    {
        BubbleSort ob = new BubbleSort();
        int mang[] = {3, 5, 6, 1, 2, 0, 8, 9, 4, 7};
        ob.bubble_sort(mang);
        for (int i=0; i<mang.length; ++i){
            System.out.print(mang[i] + " ");
        }
    }
}
