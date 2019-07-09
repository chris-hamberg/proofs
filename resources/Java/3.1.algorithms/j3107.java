import java.util.*;

public class j3107 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        Object result = lastEven(integers);
        System.out.println(result);
    }

public static Object lastEven(int[] a) {
    // Find the last even list entry.
    for (int i = a.length - 1; i > 0; i--) {
        if (a[i] % 2 == 0) {
            return i;
        }
    }
    return null;
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