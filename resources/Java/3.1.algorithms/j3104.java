public class j3104 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        int result = maxDifference(integers);
        System.out.println(result);
    }

public static int maxDifference(int[] a) {
    // Max adjacent list entry difference.
    int maximum = 0, difference;
    for (int i = 1; i < a.length; i++) {
        difference = a[i] - a[i-1];
        if (maximum < difference) {
            maximum = difference;
        }
    }
    return maximum;
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