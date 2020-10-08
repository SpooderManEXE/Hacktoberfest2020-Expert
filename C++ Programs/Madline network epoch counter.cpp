#include <iostream> 
using namespace std; 
int main() 
{ 
	// input array 
	int arr[4][2] = { { 1, 1 }, 
		{ 1, -1 }, 
		{ -1, 1 }, 
		{ -1, -1 } 
	}; 
	
	// target array 
	int t[4] = { 1, -1, -1, -1 }, i, j; 
	float yi, dif, dw1, dw2, db, w1 = 0, w2 = 0, b = 0, err[4]; 

	

	for (i = 0; i < 5; i++) 
	{ 
		float avg = 0; 
		
		cout << "EPOCH " << i + 1 << " Errors" << endl 
			<< endl; 
		for (j = 0; j < 4; j++) 
		{ 
			// calculating net input 
			yi = arr[j][0] * w1 + arr[j][1] * w2 + 1 * b; 
			dif = t[j] - yi; 
			
			// updated weights 
			w1 += 0.5 * dif * arr[j][0]; 
			w2 += 0.5 * dif * arr[j][1]; 
			b += 0.5 * dif * 1; 
			err[j] = dif * dif; 
			cout << err[j] << " "; 
			avg += err[j]; 
		} 
		cout << endl 
			<< "Total Mean Error :" << avg << endl 
			<< endl 
			<< endl; 
	} 
	return 0; 
} 
