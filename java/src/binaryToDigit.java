/**
 * Created by justin on 16. 10. 18.
 */

public class binaryToDigit {

    public boolean compareBinToHex(String binary, String hex){
        int n1 = convertToBase(binary, 2);
        int n2 = convertToBase(hex, 16);
        if (n1 < 0 || n2 <0){
            return false;
        } else {
            return n1 == n2;
        }
    }

    public int convertToBase(String number, int base){
        if (base <2 || (base > 10 && base != 16)) return -1;
        int value = 0;

        for (int i = number.length() - 1; i >=0; i--){
            int digit = digitToValue(number.charAt(i));
            if (digit < 0 || digit >= base){
                return -1;
            }
        }

        return 0;
    }

    public int digitToValue(char c){

        return 0;
    }

}


