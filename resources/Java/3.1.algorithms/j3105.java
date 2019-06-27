import java.util.*;

public class j3105 {

    public static void main(String[] a) {
        int[] integers = converter(a);
        Set result = duplicates(integers);
        System.out.println(result);
    }

public static Set duplicates(int[] a) {
    // Find duplicate list entries.
    Arrays.sort(a);
    Set<Integer> positives = new HashSet<Integer>();
    for (int i = 0; i < a.length-1; i++) {
        if (a[i] == a[i+1]) {
            positives.add(a[i+1]);
        }
    }
    return positives;
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