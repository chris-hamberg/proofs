import java.util.*;

public class j3117 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int result = firstMax(integers);
        System.out.println(result);
    }

public static int firstMax(int[] a) {
    // The first maximum integer from a list.
    int location = 0;
    int maximum = a[0];
    for (int i = 1; i < a.length; i++) {
        if (a[i] > maximum) {
            location = i;
            maximum = a[i];
        }
    }
    return location;
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