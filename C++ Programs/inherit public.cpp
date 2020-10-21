#include<iostream>
using namespace std;
class father{
	//char name[20];
	public:
		int x=40;
		void get(){
			cout<<"enter father name ";
			cin>>name;
		}
			void dis(){
				cout<<name<<"  "<<money;
			}
			protected:
					char name[20];
				float money=50;
};
class son:public father{
	int a;
	float mybalance=30;
	char myname[20];
	public:
		void get1(){
			cout<<"my Name";
		cin>>myname;
		cout<<myname<<" "<<mybalance<<endl<<name<<"  "<<money;
	}
		};
int main(){
     son s;
  cout<<"x="<<s.x<<endl;
 s.get();
 s.dis();
	return 0;
}
