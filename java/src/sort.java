import java.util.Arrays;

/**
 * Created by justin on 16. 10. 18.
 */


public class sort {

    // selection sort
    public void selectionSort(int[] array){
        int index;
        for(int i=0; i< array.length; i++){
            index = i;

            for(int j = i+1; j < array.length; j++){
                if(array[index] > array[j]){
                    index = j;
                }
            }

            int temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
        System.out.println(Arrays.toString(array));
    }
}
