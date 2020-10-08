//program to implement circular queue opertion
//A queue follows First-in-First-out principle

#include<stdio.h>
#include<stdlib.h>

struct node{
  int data;
  struct node *next;
};

void add_element(struct node **HEAD,int element){
  //Adds the element at the rear of queue
  struct node *new_node = malloc(sizeof(struct node));
  new_node->data = element;

  if((*HEAD)==NULL){
    //first node of queue
    (*HEAD)=new_node;
    (*HEAD)->next = new_node;
  }
  else{
    new_node->next = (*HEAD);
    struct node *last_node = (*HEAD);
    while(last_node->next !=(*HEAD))
      last_node = last_node->next;
    last_node->next = new_node;
  }
}

int remove_element(struct node **HEAD,int *element){
  //remove the HEAD element from the queue and saves the item to element
  //on success, returns 1, else returns 0
  if((*HEAD)==NULL)
    return 0;

  (*element)=(*HEAD)->data;
  struct node *rm_node =(*HEAD);

  if((*HEAD)==(*HEAD)->next)
    (*HEAD) = NULL;

  else{

    struct node *last_node = (*HEAD);
    while(last_node->next != (*HEAD))
      last_node = last_node->next;

    last_node->next = (*HEAD)->next;
    (*HEAD) = (*HEAD)->next;
  }

  free(rm_node);
  return 1;
}

int search(struct node *HEAD, int element){
  //searches for element in the queue and returns its position (first occurance)
  //returns -1 if the element is not found
  int position = 1;

  if(HEAD==NULL)
    return -1;

  struct node* temp = HEAD;

  do{
    if(temp->data == element)
      return position;
    position++;
    temp = temp->next;
  }while(temp!=HEAD);

  return -1;
}

void tranverse(struct node *HEAD){
  //prints the elements in the queue
  //The head is printed first
  printf("CURRENT QUEUE : ");

  if(HEAD!=NULL){
    struct node* temp = HEAD;
    do{
      printf("%d -> ",temp->data);
      temp = temp->next;
    }while(temp!=HEAD);
  }
  printf("NULL\n");
}

void destroy_queue(struct node **HEAD){
  //frees the memory allocated
  int element;
  while(remove_element(HEAD,&element));
}

void main(){
  //Menu driven program
  int element,choice=0;
  struct node *HEAD = NULL;
  while(choice!=4){
    printf("\n\nCircualar Queue opertion\n");
    printf("\t1. Add element\n");
    printf("\t2. Remove element\n");
    printf("\t3. Search element\n");
    printf("\t4. Exit\n");
    printf("Enter your choice [1-4] : ");
    scanf("%d",&choice);

    if(choice == 1){
      printf("Enter the element to add : ");
      scanf("%d",&element);
      add_element(&HEAD,element);
    }
    else if(choice == 2){
      if(remove_element(&HEAD,&element)){
        printf("Element %d is removed out\n",element);
      }
      else
        printf("UnderFlow!\n");
    }
    else if(choice == 3){
      printf("Enter the element to search : ");
      scanf("%d",&element);
      int result = search(HEAD,element);
      if(result!=-1)
        printf("Element %d found in queue at position %d \n",element,result);
      else
        printf("Element %d is not found in the queue\n",element);
    }
    tranverse(HEAD);
  }
  destroy_queue(&HEAD);
}
