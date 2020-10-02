#include <iostream>
#include <queue>

using namespace std;

class Stacks{

	queue<int> primary_queue, secondary_queue;

	public:

	void push(int element){

		secondary_queue.push(element);

		while(!primary_queue.empty()){
			secondary_queue.push(primary_queue.front());
			primary_queue.pop();
		}

		queue<int> temp_queue = primary_queue;
		primary_queue = secondary_queue;
		secondary_queue = temp_queue;
	} 

	void pop(){
		if(primary_queue.empty()){
			return;
		} else{
			primary_queue.pop();
		}
	}

	int top(){
		if(primary_queue.empty()){
			return -1;
		}else{
			return primary_queue.front();
		}
	}

	void displaystacks(){
		queue<int> temp_queue = primary_queue;
		while(!temp_queue.empty()){
			cout<<temp_queue.front()<<" ";
			temp_queue.pop();
		}
	}
};


int main(){

	Stacks s;

	s.push(1);
	s.push(2);
	s.push(3);
	s.push(4);

	s.displaystacks();

	s.pop();

	cout<<endl;

	s.displaystacks();
	return 0;
}