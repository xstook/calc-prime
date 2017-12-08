#include <iostream>
#include <math.h>
#include <ctime>
#include <iomanip>
#include <locale>
using namespace std;



int is_prime(unsigned long long n);


int main(){
	stringstream ss;
	ss.imbue(locale(""));

	clock_t start_time = clock();
	unsigned long long number = 2; 
	for (unsigned long long number = 2; number < 10000000; number++) {
		unsigned long long result = is_prime(number);
		if (result != 0){
			ss << fixed << result;
			cout << "\rLargest prime found is " << ss.str() << "  ";
			ss.str("");
		}
	}

	double duration = (clock() - start_time) / (double)CLOCKS_PER_SEC;

	cout << "\nIt took " << duration << " seconds to finish";
	cout << "\nScore: " << 1 / duration * 1000 << "\n";
	return 0;
}




int is_prime(unsigned long long n){
	if (n == 1){
		return 0;
	}
	else if (n == 2) {
		return n;
	}
	else if (n > 2 && (n % 2 == 0)){
		return 0;
	}

	unsigned long long max_divisor = floor(sqrt(n));
	for(unsigned long long i = 3; i < max_divisor + 1; i = i + 2){
		if (n % i == 0){
			return 0;
		}
	}

	return n;

}
