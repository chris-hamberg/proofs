import java.util.*;

public class j3118 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int result = lastMin(integers);
        System.out.println(result);
    }

public static int lastMin(int[] a) {
    // The last smallest integer from a list.
    int location = a.length - 1;
    int minimum = a[location];
    for (int i = a.length - 1; i > -1; i--) {
        if (a[i] < minimum) {
            location = i;
            minimum = a[i];
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