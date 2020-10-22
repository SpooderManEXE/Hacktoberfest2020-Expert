//program to implement stack opertion
//A stack follows Last-in-First-out principle

#include<stdio.h>
#include<stdlib.h>

struct node{
  int data;
  struct node *next;
};

void push(struct node **TOP,int element){
  //Pushes the element at the top of the stack
  struct node *new_node = malloc(sizeof(struct node));
  new_node->data = element;
  new_node->next = (*TOP);
  (*TOP)=new_node;
}

int pop(struct node **TOP,int *element){
  //Pops the top element from the stack and saves the item to element
  //on success, returns 1, else returns 0
  if((*TOP)==NULL)
    return 0;

  (*element)=(*TOP)->data;
  struct node *rm_node =(*TOP);
  (*TOP)=(*TOP)->next;
  free(rm_node);
  return 1;
}

int search(struct node *TOP, int element){
  //searches for element in the stack and returns its position (first occurance)
  //returns -1 if the element is not found
  int position = 1;
  while(TOP!=NULL){
    if(TOP->data == element)
      return position;
    TOP = TOP->next;
    position++;
  }
  return -1;
}

void tranverse(struct node *TOP){
  //prints the elements in the stack.
  //The top is printed first
  printf("CURRENT STACK : ");
  while(TOP!=NULL){
    printf("%d -> ",TOP->data);
    TOP = TOP->next;
  }
  printf("NULL\n");
}

void destroy_stack(struct node **TOP){
  //frees the memory allocated
  int element;
  while(pop(TOP,&element));
}

void main(){
  //Menu driven program
  int element,choice=0;
  struct node *TOP = NULL;
  while(choice!=4){
    printf("\n\nStack opertion\n");
    printf("\t1. Push element\n");
    printf("\t2. Pop element\n");
    printf("\t3. Search element\n");
    printf("\t4. Exit\n");
    printf("Enter your choice [1-4] : ");
    scanf("%d",&choice);

    if(choice == 1){
      printf("Enter the element to push : ");
      scanf("%d",&element);
      push(&TOP,element);
    }
    else if(choice == 2){
      if(pop(&TOP,&element)){
        printf("Element %d is popped out\n",element);
      }
      else
        printf("UnderFlow!\n");
    }
    else if(choice == 3){
      printf("Enter the element to search : ");
      scanf("%d",&element);
      int result = search(TOP,element);
      if(result!=-1)
        printf("Element %d found in stack at position %d \n",element,result);
      else
        printf("Element %d is not found in the stack\n",element);
    }
    tranverse(TOP);
  }
  destroy_stack(&TOP);
}
