import java.util.*;

public class j3116 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int result = min(integers);
        System.out.println(result);
    }

public static int min(int[] a) {
    // Find the least element in a sequence of 
    // natural numbers.
    int minimum = a[0];
    for (int i = 1; i < a.length; i++) {
        if (a[i] < minimum) {
            minimum = a[i];
        }
    }
    return minimum;
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