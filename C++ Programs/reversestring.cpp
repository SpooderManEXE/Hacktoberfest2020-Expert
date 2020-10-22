#include <iostream>
#include <stack>


class Stacks{
private:
	char A[100];
	int top;
public:
	void push(char x);
	void pop();
	int Top();
	bool isempty();
};

void push(char x){

}

int length(char C[]){
	int length = 0;
	for(int i = 0; C[i] != '\0'; i++ ){
		length++;
	}
	return length;
}

void Reverse(char C[], int size){
	Stacks s;
	for(int i =0 ;i<size ; i++){
		s.push(C[i]);
	}

	for(int i =0 ; i<size;i++){
		C[i] = s.Top();
		s.pop();
	}
}


int main(){

	char array[] = "Gaurav";
	Reverse(array, length(array));

	return 0;
}