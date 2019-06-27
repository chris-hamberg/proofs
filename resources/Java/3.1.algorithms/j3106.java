import java.util.*;

public class j3106 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int result = negatives(integers);
        System.out.println(result);
    }

public static int negatives(int[] a) {
    // Count negative list entries.
    int count = 0;
    for (int i = 0; i < a.length; i++) {
        if (a[i] < 0) {
            count++;
        }
    }
    return count;
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