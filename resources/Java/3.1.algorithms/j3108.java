import java.util.*;

public class j3108 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        Integer result = largestEven(integers);
        System.out.println(result);
    }

public static Integer largestEven(int[] a) {
    // Find the largest even list entry.
    Integer index = null;
    for (int i = 0; i < a.length; i++) {
        if (a[i] % 2 == 0) {
            if ((index == null) || (a[i] > a[index])) {
                index = i;
            }
        }
    }
    return index;
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