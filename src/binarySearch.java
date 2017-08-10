/**
 * Created by justin on 16. 10. 18.
 */
public class binarySearch {
    public static int ibnarySearch(int[] a, int x) {
        int low = 0;
        int high = a.length - 1;
        int mid;

        while (low <= high) {
            mid = (low + high) / 2;
            if (a[mid] < x) {
                low = mid + 1;
            } else if (a[mid] > x) {
                high = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arrayInt = {1,2,3,4,5,6};
        int index = ibnarySearch(arrayInt,4);
        if (index < 0){
            System.out.println("not machting");
        }else{
            System.out.println(arrayInt[index]);
        }
    }
}
