#include<iostream>

class inter {
private:
	int i;
	const char* p;
public:

	inter(int i, const char* p) :i{ i }, p{ p } {};
	virtual void func() {
		std::cout << *(this->p)<<"\n";
		std::cout << this->i;
	}
};

class inherit : inter {
private:
	int i;
	const char* p;
public:
	inherit(int i,const char*p) :inter(i, p) {};
	
	void func() {
		std::cout << "This is polymorphism\n";
	}
};

int main(){
	const char var = 'p';
	const char* ch=&var;
	inherit* obj1 = new inherit(67,ch);
	inter* obj2 = new inter(67, ch);
	obj1->func();
	obj2->func();
	std::cin.get
}