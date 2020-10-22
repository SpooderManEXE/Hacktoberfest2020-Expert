#include<bits/stdc++.h>
using namespace std ;
#define ll long long
#define rep(i,a) for(i = 0 ; i < a ; i++)
#define whln(t) while(t--)
#define whlp(t) while(t++)
int i ;
void Merging_Sorted_List(int arr[],int a,int b,int c,int d){
  int temp[d-a+1];
  int j = a,o=c ;
  for(int i = 0 ; i<=d-a;i++){        // like the name suggests we will be merging
                                     //  the sorted lists  
      if(o==d+1){                           
        temp[i]= arr[j];
        j++;
        continue;
      }
      else if(j==b+1){
        temp[i] = arr[o];
        o++;
        continue;
      }

      if(arr[j]<=arr[o]){
        temp[i]=arr[j];
        j++;
      }
      else if(arr[o]<arr[j]){
          temp[i]=arr[o];
          o++;
      }
  }
   for(int i = 0 ; i<=d-a;i++)
      arr[i+a]= temp[i];
}

void Break_Sort_Individual_List(int arr[],int a,int b){
  if((b-a)<=1){
    // Merging_Sorted_List(arr,a,abs(a-b)/2,abs(a-b)/2 +1,b);
    return ; // start merging when only 1 element left in each section
  }
  Break_Sort_Individual_List(arr,a,abs(a-b)/2);          // first we will break it and sort it 
  Break_Sort_Individual_List(arr,abs(a-b)/2 +1,b);
  Merging_Sorted_List(arr,a,abs(a-b)/2,abs(a-b)/2 +1,b);      // then merge it 
}  

int main(){
  #ifndef ONLINE_JUDGEz
    // for getting input from input.txt
    freopen("input1.txt", "r", stdin);
    // for writing output to output.txt
    freopen("output1.txt", "w", stdout);
  #endif


    //your code here
    return 0;
}