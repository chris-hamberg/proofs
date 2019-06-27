import java.util.*;

public class j3111 {

    public static void main(String[] a) {
        //int[] integer = converter(a);
        String x = a[0], y = a[1];
        Object[] result = swap(x, y);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }

public static Object[] swap(Object x, Object y) {
    // Swap x and y.
    Object[] swapped = new Object[2];
    Object temp = x;
    x = y;
    y = temp;
    swapped[0] = x; swapped[1] = y;
    return swapped;
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