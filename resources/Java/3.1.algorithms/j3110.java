import java.util.*;

public class j3110 {

    public static void main(String[] a) {
        //int[] integer = converter(a);
        int n = Integer.parseInt(a[0]), x = Integer.parseInt(a[1]);
        double result = power(n, x);
        System.out.println(result);
    }

public static double power(int n, int x) {
    // Compute x**n
    int exponent = Math.abs(n);
    double product = 1;
    while (exponent > 0) {
        product *= x;
        exponent--;
    }
    if (n < 0) {
        return 1 / product;
    }
    return product;
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