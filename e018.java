import java.util.ArrayList;
import java.util.List;

public class e018 {

    public static void main(String []args) {

        List<Integer> sum = new ArrayList<Integer>();
        int[] row_1 = {75};
        int[] row_2 = {95, 64};
        int[] row_3 = {17, 47, 82};
        int[] row_4 = {18, 35, 87, 10};
        int[] row_5 = {20, 4, 82, 47, 65};
        int[] row_6 = {19, 1, 23, 75, 3, 34};
        int[] row_7 = {88, 2, 77, 73, 7, 63, 67};
        int[] row_8 = {99, 65, 4, 28, 6, 16, 70, 92};
        int[] row_9 = {41, 41, 26, 56, 83, 40, 80, 70, 33};
        int[] row_10 = {41, 48, 72, 33, 47, 32, 37, 16, 94, 29};
        int[] row_11 = {53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14};
        int[] row_12 = {70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57};
        int[] row_13 = {91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48};
        int[] row_14 = {63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31};
        int[] row_15 = {4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23};

        int max = 0;
        int max_a = row_1[0];
        int max_b = 0;
        int max_c = 0;
        int max_d = 0;
        int max_e = 0;
        int max_f = 0;
        int max_g = 0;
        int max_h = 0;
        int max_i = 0;
        int max_j = 0;
        int max_k = 0;
        int max_l = 0;
        int max_m = 0;
        int max_n = 0;
        int max_o = 0;

        int temp = 0;
        int counter = 0;
        //for (int a = 0; a < row_1.length; a++) {
            for (int b = 0; b < row_2.length; b++) {
                for (int c = b; c <= b + 1; c++) {
                    for (int d = c; d <= c + 1; d++) {
                        for (int e = d; e <= d + 1; e++) {
                            for (int f = e; f <= e + 1; f++) {
                                for (int g = f; g <= f + 1; g++) {
                                    for (int h = g; h <= g + 1; h++) {
                                        for (int i = h; i <= h + 1; i++) {
                                            for (int j = i; j <= i + 1; j++) {
                                                for (int k = j; k <= j + 1; k++) {
                                                    for (int l = k; l <= k + 1; l++) {
                                                        for (int m = l; m <= l + 1; m++) {
                                                            for (int n = m; n <= m + 1; n++) {
                                                                for (int o = n; o <= n + 1; o++) {
                                                                    counter = counter + 1;
                                                                    temp = row_1[0] + row_2[b] + row_3[c] +
                                                                            row_4[d] + row_5[e] + row_6[f] +
                                                                            row_7[g] + row_8[h] + row_9[i] +
                                                                            row_10[j] + row_11[k] + row_12[l] +
                                                                            row_13[m] + row_14[n] + row_15[o];
                                                                    if (temp > max) {
                                                                        max = temp;
                                                                        max_b = row_2[b];
                                                                        max_c = row_3[c];
                                                                        max_d = row_4[d];
                                                                        max_e = row_5[e];
                                                                        max_f = row_6[f];
                                                                        max_g = row_7[g];
                                                                        max_h = row_8[h];
                                                                        max_i = row_9[i];
                                                                        max_j = row_10[j];
                                                                        max_k = row_11[k];
                                                                        max_l = row_12[l];
                                                                        max_m = row_13[m];
                                                                        max_n = row_14[n];
                                                                        max_o = row_15[o];
                                                                    }
                                                                    System.out.println(counter);
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
                    }
                }
            }
        //}

        System.out.println("Results!");
        System.out.println(max);
        System.out.println(max_a);
        System.out.println(max_b);
        System.out.println(max_c);
        System.out.println(max_d);
        System.out.println(max_e);
        System.out.println(max_f);
        System.out.println(max_g);
        System.out.println(max_h);
        System.out.println(max_i);
        System.out.println(max_j);
        System.out.println(max_k);
        System.out.println(max_l);
        System.out.println(max_m);
        System.out.println(max_n);
        System.out.println(max_o);

    }
}
