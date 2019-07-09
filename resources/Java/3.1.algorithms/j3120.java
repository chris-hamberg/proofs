import java.util.*;

public class j3120 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int[] result = extrema(integers);
        System.out.println(Arrays.toString(result));
    }

public static int[] extrema(int[] a) {
    // Find the extrema from a sequence of integers.
    int minimum = a[0], maximum = a[0];
    for (int i = 1; i < a.length; i++) {
        if (a[i] < minimum) {
            minimum = a[i];
        } else if (a[i] > maximum) {
            maximum = a[i];
        }
    }
    int[] result = {minimum, maximum};
    return result;
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