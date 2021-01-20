import java.text.DecimalFormat;
import java.text.NumberFormat;

public class Primes {

	public static void main(String[] args) {
		NumberFormat formatter = new DecimalFormat("#############.######");

		boolean doAll = false;

		if (doAll) {
			for (int lcv = 1; lcv <= 9; lcv++) {
				int count = (int) Math.pow(10, lcv);
				double timeElapsed = primes(count);
				System.out.println(setw("" + count, 13) + " " + setw(formatter.format(timeElapsed), 30));
			}
		} else {
			
		}
	}

	public static double primes(int count) {
		int[] prime_array = new int[count];

		prime_array[0] = 2;
		prime_array[1] = 3;

		int current_count = 2, test_num = 5, k = 0;

		boolean is_prime = true;

		double startTime = (double) System.nanoTime();

		while (current_count < count) {
			while (prime_array[k] <= Math.sqrt(test_num)) {
				if (test_num % prime_array[k] == 0) {
					is_prime = false;
					break;
				}
				k = k + 1;
			}
			if (is_prime) {
				prime_array[current_count] = test_num;
				current_count = current_count + 1;
			} else {
				is_prime = true;
			}

			if ((test_num + 1) % 6 == 0) {
				test_num = test_num + 2;
			} else {
				test_num = test_num + 4;
			}

			test_num += 1;
			k = 0;
		}

		double endTime = (double) System.nanoTime();
		return (endTime - startTime) / Math.pow(10, 9);
	}

	public static String setw(String string, int length) {
		while (string.length() < length) {
			string = " " + string;
		}
		return string;
	}

}
