import java.util.Arrays;

/**
 * Created by justin on 16. 10. 17.
 */

public class Main {

    public static void main(String[] args){

        System.out.println("Hello Wrold");
        boolean result = isUniqueChars2("aabb");
        System.out.println(result);

        String[] words = {"abcde", "hello", "apple", "kite", "padle"};
        for (String word : words) {
            System.out.println(word + ": " + isUniqueChars2(word));
        }

        swapMinMax mSwap = new swapMinMax();
        int[] sequnceInt = {1,2,3,4,5};

        //mSwap.swapMinMax(sequnceInt);
        mSwap.improvedSwapMinMax(sequnceInt);

        System.out.println(Arrays.toString(sequnceInt));

        sort mSort = new sort();
        int[] intArray = {1,3,2,4,5};
        System.out.println("before sorting: "+Arrays.toString(intArray));
        mSort.selectionSort(intArray);

        int resultInt = 7 / 2 ;
        System.out.println(resultInt);

    }



    static public boolean isUniqueChars2 (String str){
        if (str.length() > 256) return false;

        boolean[] char_set = new boolean[256];

        for (int i = 0; i < str.length(); i++){
            int var = str.charAt(i);
            if(char_set[var]){
                return false;
            }
        char_set[var] = true;
        }
        return true;
    }
}
