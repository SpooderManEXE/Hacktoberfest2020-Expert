#include <iostream>
using namespace std;
int noOfDigit(long x) {
   int n = 0;
   while (x > 0) {
      x /= 10;
      n++;
   }
   return n;
}
void schonhageStrassenMultiplication(long a, long b, int n, int m) {
   int linearConvolution[n + m - 1];
   for (int i = 0; i < (n + m - 1); i++)
      linearConvolution[i] = 0;
      long p = a;
   for (int i = 0; i < m; i++) {
      a = p;
      for (int j = 0; j < n; j++) {
         linearConvolution[i + j] += (b % 10) * (a % 10);
         a /= 10;
      }
      b /= 10;
   }
   cout << "The Linear Convolution is: ( ";
   for (int i = (n + m - 2); i >= 0; i--) {
      cout << linearConvolution[i] << " ";
   }
   cout << ")";
   long product = 0;
   int nextCarry = 0, base = 1;
   for (int i = 0; i < n + m - 1; i++) {
      linearConvolution[i] += nextCarry;
      product = product + (base * (linearConvolution[i] % 10));
      nextCarry = linearConvolution[i] / 10;
      base *= 10;
   }
   cout << "\nThe Product of the numbers is: " << product;
}
int main(int argc, char **argv) {
   cout << "Enter the numbers:";
   long a, b;
   cin >> a >> b;
   int n = noOfDigit(a);
   int m = noOfDigit(b);
   schonhageStrassenMultiplication(a, b, n, m);
}
