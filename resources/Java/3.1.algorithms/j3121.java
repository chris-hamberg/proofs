import java.util.*;

public class j3121 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int[] result = partialSort(integers);
        System.out.println(Arrays.toString(result));
    }

public static int[] partialSort(int[] a) {
    // Sort the first 3 terms in a.
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2 - i; j++) {
            if (a[j] > a[j+1]) {
                int temp = a[j+1];
                a[j+1] = a[j];
                a[j] = temp;
            }
        }
    }
    return a;
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