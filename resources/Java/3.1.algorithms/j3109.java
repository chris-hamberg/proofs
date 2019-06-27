import java.util.*;

public class j3109 {

    public static void main(String[] a) {
        //int[] integer = converter(a);
        boolean result = palindrome(a[0]);
        System.out.println(result);
    }

public static boolean palindrome(String a) {
    // Determine whether a string in a palindrome.
    int right  = a.length() - 1;
    int limit  = Math.floor(a.length() / 2);
    for (int i = 0; i < limit; i++) {
        if (a.charAt(i) !=  a.charAt(right - i)) {
            return false;    
        }
    }
    return true;
}

    public static int[] converter(String[] a){
        // This is just preprocessing the input
        int size = a.length;
        int[] integers = new int[size];
        for (int i = 0; i < size; i++) {
            integers[i] = Integer.parseInt(a[i]);
        }
        return integers;
    }

}