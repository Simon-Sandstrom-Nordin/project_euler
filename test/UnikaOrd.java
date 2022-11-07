package test;

// Input:   1) Först ett heltal N som är längden på eftersökta delföljden.
//          2) Sträng (1 till 10^7 tecken lång) vilken är en teckenföljd.
// Output:  Siffra som anger startpositionen hos delföljd av efterfrågad längd.
//          Indexeringen startar vid noll. -1 ges om ingen sådan följd finns.


import java.util.*;

public class UnikaOrd {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        String string = sc.next();

        Integer index = index_finder(length, string);
        System.out.println(index);

    }

    private static int index_finder(int length, String string) {
        // System.out.println(length);
        // System.out.println(string);

        // I got a list that'll hold all sequences
        List<String> list = new ArrayList<String>();
        Set<String> set_of_duplicates = new HashSet<String>();  // wtf is a LinkedHashSet?

        int index = 0;  // start at one, nvm from 0
        Boolean searching = true;
        while (searching) {
            String substring = string.substring(index, index + length);

            if (list.contains(substring)) {
                set_of_duplicates.add(substring);
            } else {
                list.add(substring);
            }

            index = index + 1;
            if (index == string.length() - length) {
                searching = false;  // actually correct I think, otherwise index+1 is out of bounds.
            }
        }

        // convert list into list_but_set
        Set<String> list_but_set = new HashSet<String>();
        for (int k = 0; k < list.size(); k++) {
            list_but_set.add(list.get(k));
        }   // indexing in ArrayList starts at 0. Not like MATLAB's 1 for vectors.

        // get difference. Actually, mutilate this set.
        list_but_set.removeAll(set_of_duplicates);  // This mutilates, but that's ok.

        // Now search and return index, then we're done! Hopefully.
        index = 0;  // start at one
        searching = true;
        while (searching) {
            String substring = string.substring(index, index + length);

            if (list_but_set.contains(substring)) {
                return index + 1;
            }

            index = index + 1;
            if (index + length == string.length()) {
                searching = false;  // actually correct I think, otherwise index+1 is out of bounds.
                // I was in the wrong. I was wrong. I wrongly did this.
                // Or maybe I was in the right, I increment later.
            }
        }

        // If no such delföljd exists.
        return -1;
    }

}

// notes on java: String max length is 2147483647. Min is 0. Our limit is 10 million. Dats ok.

// After trying in Kattis, first two test cases are correct but the third one
// gets a Run-Time Error. It also worked for the 3 shits they gave me.
// Conclusion: it works but to pass this task I need to make the
// algorithm more efficient.

// Aja... den fungerar bättre nu iallafall, men Kattis visar 404: Not Found
