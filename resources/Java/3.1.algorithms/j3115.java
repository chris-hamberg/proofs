import java.util.*;

public class j3115 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int x = Integer.parseInt(a[0]);
        int[] result = insert(x, integers);
        System.out.println(Arrays.toString(result));
    }

public static int[] insert(int x, int[] a) {
    // Insert an integer x at the correct index
    // position in a list of integers in increasing
    // order.
    Arrays.sort(a);
    a = Arrays.copyOf(a, a.length + 1);
    if (a[a.length - 2] <= x) {
        a[a.length - 1] = x;
    } else {
        int i = a.length - 2;
        while ((i + 1 > 0) && (x < a[i])) {
            a[i+1] = a[i];
            i--;
        }
        a[i+1] = x;
    }
    return a;
}

    public static int[] converter(String[] a){
        // This is just preprocessing the input
        int size = a.length - 1;
        int[] integers = new int[size];
        for (int i = 0; i < size; i++) {
            integers[i] = Integer.parseInt(a[i+1]);
        }
        return integers;
    }

}