/*It is a data structure code...topic named Priority Queue
We can add elements in any order by specifying the priority of the elements in queue*/

#include<stdio.h>
#include<stdlib.h>

int pQ[20][30]; 
int rear = -1;
int front = -1;

void insert(int, int);
int pop1();
void display();
void setValue(int, int, int);

int main(){
    int ch, element,pr, pop;
    printf("\n");
    while(1){
        printf("\n**  OPERATIONS  **\n");
        printf("\n 1.Insert\n 2.Delete\n 3.Display\n 4.Exit\n Enter your choice: ")
        scanf("%d", &ch);
        switch(ch){
            case 1: printf("Enter the value and its priority");
                    scanf("%d", &pr);
                    insert(element, pr);
                    break;
            case 2: pop = pop1();
                    printf("\n Deleted item is:  %d", pop);
                    break;
            case 3: printf("\nPriority Queue is : \t");
                    display();
                    break;
            case 4: exit(1);
                    break;
            default: printf("\nInvalid Choice");
                    break;
        }
    }
    return 0;
}

void setValue(int i, int element, int pr){
    int j;
    for(j=rear-1; j>=i; j--){
        pQ[j+1][0]=pQ[j][0];
        pQ[j+1][1]=pQ[j][1];
    }
    pQ[i][0]=element;
    pQ[i][1]=pr;

}

void insert(int element, int pr){
    if(rear==14 ){
        printf("\nYour queue is full..");
    }
    else if(rear==-1){
        rear++;
        front++;
        pQ[rear][0]=element;
        pQ[rear][1]=pr;
    }
    else {
        int i ;
        rear++;
        if(pQ[0][1]>pr && rear ==1){
            pQ[rear][0]=element;
            pQ[rear][1]=pr;
        }
        else if(pQ[0][1]<pr && rear == 1){
            pQ[rear][0]=pQ[rear-1][0];
            pQ[rear][1]=pQ[rear-1][1];
            pQ[rear-1][0]=element;
            pQ[rear-1][1]=pr;
        }
        else if(rear >1){
            for(i=0; i<=rear; i++){
                if((i!=rear-1) && (pQ[i][1]>=pr && pQ[i+1][1]<pr)){
                    setValue(i+1,element, pr);
                    break;
                }
                if((i!=rear-1) && (pQ[i][1]>pr && pQ[i+1][1]<=pr)){
                    setValue(i+2,element, pr);
                    break;
                }
                else if((i!=rear-1) && (pQ[i][1]<pr) ){
                    setValue(i,element, pr);
                    break;
                }
                else if(i==rear-1){
                    pQ[rear][0]=element;
                    pQ[rear][1]=pr;
                    break;
                }
            }
        }
    }
}
int pop1(){
    if(front==-1 || front>rear){
        printf("\nUnderflow");
    }
    else{
        int popOut = pQ[front][0];
        front++;
        return popOut;
    }
}
 void display(){
     if(front==-1){
         printf("\nEmpty Queue..");
     }
     else {
         int k,j;
         for(k=front; k<=rear; k++){
            for(j=0; j<2; j++){
                printf("%d\t", pQ[k][j]);
                if(j==1){
                    printf("\n");
                }
            }
         }
     }
 }
