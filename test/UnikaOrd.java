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
        System.out.println(length);
        System.out.println(string);

        // I got a list
        List<String> list = new ArrayList<String>();
        List<String> list = new List<String>() {
            @Override
            public int size() {
                return 0;
            }

            @Override
            public boolean isEmpty() {
                return false;
            }

            @Override
            public boolean contains(Object o) {
                return false;
            }

            @Override
            public Iterator<String> iterator() {
                return null;
            }

            @Override
            public Object[] toArray() {
                return new Object[0];
            }

            @Override
            public <T> T[] toArray(T[] a) {
                return null;
            }

            @Override
            public boolean add(String s) {
                return false;
            }

            @Override
            public boolean remove(Object o) {
                return false;
            }

            @Override
            public boolean containsAll(Collection<?> c) {
                return false;
            }

            @Override
            public boolean addAll(Collection<? extends String> c) {
                return false;
            }

            @Override
            public boolean addAll(int index, Collection<? extends String> c) {
                return false;
            }

            @Override
            public boolean removeAll(Collection<?> c) {
                return false;
            }

            @Override
            public boolean retainAll(Collection<?> c) {
                return false;
            }

            @Override
            public void clear() {

            }

            @Override
            public boolean equals(Object o) {
                return false;
            }

            @Override
            public int hashCode() {
                return 0;
            }

            @Override
            public String get(int index) {
                return null;
            }

            @Override
            public String set(int index, String element) {
                return null;
            }

            @Override
            public void add(int index, String element) {

            }

            @Override
            public String remove(int index) {
                return null;
            }

            @Override
            public int indexOf(Object o) {
                return 0;
            }

            @Override
            public int lastIndexOf(Object o) {
                return 0;
            }

            @Override
            public ListIterator<String> listIterator() {
                return null;
            }

            @Override
            public ListIterator<String> listIterator(int index) {
                return null;
            }

            @Override
            public List<String> subList(int fromIndex, int toIndex) {
                return null;
            }

            // This is the equivalent of drawing for fun, experiment and see
            // what happens, right? Apparently there's an @Override in Java.
            // Whatever that is. With built-in static methods and shit.
            // Apparently java considers "shit" an offensive word :D.

        };

        // If no such delföljd exists.
        return -1;
    }

}
