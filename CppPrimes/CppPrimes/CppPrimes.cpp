#include <iostream>
#include <iomanip>
#include <chrono>
#include <thread>

using namespace std;


class Timer
{
public:
	Timer() : beg_(clock_::now()) {}
	void reset() { beg_ = clock_::now(); }
	double elapsed() const {
		return std::chrono::duration_cast<second_>
			(clock_::now() - beg_).count();
	}

private:
	typedef std::chrono::high_resolution_clock clock_;
	typedef std::chrono::duration<double, std::ratio<1> > second_;
	std::chrono::time_point<clock_> beg_;
};

void longlongs(unsigned long long count);

int main() {

	unsigned long long count;
	for (int lcv = 1; lcv <= 9; lcv++) {
		longlongs(pow(10, lcv));
		std::chrono::seconds dura(5);
		std::this_thread::sleep_for(dura);
	}
}

void longlongs(unsigned long long count) {
	Timer tmr;

	unsigned long long* prime_array = new unsigned long long[count];

	prime_array[0] = 2;
	prime_array[1] = 3;

	long long current_count = 2, test_num = 5, k = 0;

	bool is_prime = true;

	tmr.reset();
	while (current_count < count) {
		while (prime_array[k] <= sqrt(test_num)) {
			if (test_num % prime_array[k] == 0) {
				is_prime = false;
				break;
			}
			k = k + 1;
		}
		if (is_prime) {
			prime_array[current_count] = test_num;
			current_count = current_count + 1;
		}
		else {
			is_prime = true;
		}

		if ((test_num + 1) % 6 == 0) {
			test_num = test_num + 2;
		}
		else {
			test_num = test_num + 4;
		}

		test_num += 1;
		k = 0;
	}

	cout << setw(13) << count << " " << setw(30) << fixed << tmr.elapsed() << endl;
	delete[] prime_array;
}
