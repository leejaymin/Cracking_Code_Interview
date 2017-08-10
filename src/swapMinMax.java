/**
 * Created by justin on 16. 10. 18.
 */
public class swapMinMax {

    public void swapMinMax(int[] array){
        // to compute min value
        int minIndex = 0;
        for (int i = 1; i < array.length; i++){
            if(array[i] < array[minIndex]){
                minIndex = i;
            }
        }

        // to comput max value
        int maxIndex = 0;
        for (int i = 1; i < array.length; i++){
            if(array[i] > array[maxIndex]){
                maxIndex = i;
            }
        }

        // exchange between min and max
        int temp = array[minIndex];
        array[minIndex] = array[maxIndex];
        array[maxIndex] = temp;
    }


    // refactoring swapMinMax code
    public void improvedSwapMinMax(int[] array){
        int minIndex = getMinIndex(array);
        int maxIndex = getMaxIndex(array);
        exchange(array,minIndex,maxIndex);
    }

    public int getMinIndex(int[] array){
        int minIndex = 0;

        for(int i=0; i < array.length; i++){
            if(array[minIndex] > array[i]){
                minIndex = i;
            }
        }
        return minIndex;
    }

    public int getMaxIndex(int[] array){
        int maxIndex = 0;

        for(int i=0; i < array.length; i++){
            if(array[maxIndex] < array[i]){
                maxIndex = i;
            }
        }
        return maxIndex;

    }
    public void exchange(int[] array,int minIndex, int maxIndex){
        int temp = array[minIndex];
        array[minIndex] = array[maxIndex];
        array[maxIndex] = temp;
    }
}
