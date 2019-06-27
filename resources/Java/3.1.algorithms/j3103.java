public class j3103 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int total = sum(integers);
        System.out.println(total);
    }

public static int sum(int[] a) {
    // Calculate the sum of integers in a list.
    int total = 0;
    for (int i = 0; i < a.length; i++) {
        total = total + a[i];
    }
    return total;
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