package garbage;

import java.util.ArrayList;
import java.util.List;

public class lexicographic_trial {

    public static void main(String []args) {

        List<Integer> numbers = new ArrayList<Integer>();

        for (int k = 0; k < 9; k++) {
            numbers.add(k);
        }

        List<String> sorted = new ArrayList<String>();

        for (int a = 0; a <= numbers.size(); a++) {
            for (int b = 0; b <= numbers.size(); b++) {
                for (int c = 0; c <= numbers.size(); c++) {
                    for (int d = 0; d <= numbers.size(); d++) {
                        for (int e = 0; e <= numbers.size(); e++) {
                            for (int f = 0; f <= numbers.size(); f++) {
                                for (int g = 0; g <= numbers.size(); g++) {
                                    for (int h = 0; h <= numbers.size(); h++) {
                                        for (int i = 0; i <= numbers.size(); i++) {
                                            for (int j = 0; j <= numbers.size(); j++) {
                                                if (a != b && a != c && a != d && a != e & a != f && a != g && a != h && a != i && a != j
                                                        && b != c && b != d && b != e && b != f && b != g && b != h && b != i && b != j
                                                        && c != d && c != e && c != f && c != g && c != h && c != i && c != j
                                                        && d != e && d != f && d != g && d != h && d != i && d != j
                                                        && e != f && e != g && e != h && e != i && e != j
                                                        && f != g && f != h && f != i && f != j
                                                        && g != h && g != i && g != j
                                                        && h != i && h != j
                                                        && i != j) {
                                                    String A = Integer.toString(a);
                                                    String B = Integer.toString(b);
                                                    String C = Integer.toString(c);
                                                    String D = Integer.toString(d);
                                                    String E = Integer.toString(e);
                                                    String F = Integer.toString(f);
                                                    String G = Integer.toString(g);
                                                    String H = Integer.toString(h);
                                                    String I = Integer.toString(i);
                                                    String J = Integer.toString(j);
                                                    sorted.add(A + B + C + D + E + F + G + H + I + J);
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        // for (int k = 0; k < sorted.size(); k++) {
        //     System.out.println(sorted.get(k));
        // }

        System.out.println(sorted.get(1000000-1));

    }

}
