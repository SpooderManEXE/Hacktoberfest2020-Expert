
// Java program for Pascal's Triangle 
// A O(n^2) time and O(1) extra  

import java.io.*; 

class PascalTriangle { 
  public static void printPascal(int n){ 
    for(int line = 1; line <= n; line++) 
    {     
      int C=1;
      for(int i = 1; i <= line; i++) 
      {  
        System.out.print(C+" "); 
        C = C * (line - i) / i;  
      } 
    System.out.println(); 
    } 
  } 
  public static void main (String[] args) { 
    int n = 5; 
    printPascal(n); 
  }  
} 
