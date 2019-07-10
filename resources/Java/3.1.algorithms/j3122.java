import java.util.*;

public class j3122 {

    public static void main(String[] a) {
        //int[] integers = converter(a);
        String sentence = merger(a);
        int result = longestWord(sentence);
        System.out.println(result);
    }

public static int longestWord(String a) {
    //Find the longest word.
    int wordLength = 0, maximumSize = 0;
    int maximumIndex = 0;
    a += "\u0020";
    for (int i = 0; i < a.length(); i++) {
        if (a.charAt(i) != '\u0020')  {
            wordLength += 1;
        } else {
            int index = i - wordLength;
            if (wordLength > maximumSize) {
                maximumSize = wordLength;
                maximumIndex = index;
            }
            wordLength = 0;
        }
    }
    return maximumIndex;
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

    public static String merger(String[] a) {
        String merged = "";
        for (String word: a) {
            merged += word + " ";
        }
        return merged;
    }

}