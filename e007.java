import java.util.ArrayList;
import java.util.List;

public class e007 {

    static List<Integer> known_primes = new ArrayList<Integer>();


    public static void main(String []args) {

        int counter = 2;
        while (known_primes.size() < 10001) {
            if (check_primality(counter) == true) {
                known_primes.add(counter);
            } else {
                counter += 1;
            }

        }

        System.out.println(known_primes.get(known_primes.size() - 1));

        for (int k = 0; k < known_primes.size(); k++) {

            System.out.println(known_primes.get(k));

        }

    }

    // public static

    public static boolean check_primality(int candidate_prime) {

        for (int k = 0; k < known_primes.size(); k++) {
            if (known_primes.get(k) == candidate_prime) {
                return false;
            }
        }   // checks if I've already discovered that prime

        if (candidate_prime == 2) {
            return true;
        }

        for (int k = 2; k < candidate_prime; k++) {
            if (candidate_prime % k == 0) {
                return false;
            }
        }

        return true;

    }

}
