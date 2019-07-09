import java.util.*;

public class j3119 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int x = integers[0];
        int y = integers[1];
        int z = integers[2];
        int[] result = stats(x, y, z);
        System.out.println(Arrays.toString(result));
    }

public static int[] stats(int x, int y, int z) {
    // Max, median, mean, and min.
    int[] a = {x, y, z};
    for (int i = 0; i < a.length - 1; i++) {
        for (int j = 0; j < a.length - i - 1; j++) {
            if (a[j] > a[j+1]) {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
    int minimum = a[0], maximum = a[a.length - 1];
    int mean = (a[0] + a[1] + a[2]) / a.length;
    int median = a[1];
    int[] result = {maximum, median, mean, minimum};
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