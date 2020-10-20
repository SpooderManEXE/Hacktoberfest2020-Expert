#include <stdio.h>
struct node
{
    int num;
    struct node *link;
};
void insert(int n);
void reverse();
void display();
void main()
{
    int n;
	printf("enter number of nodes: ");
    scanf("%d", &n);
    insert(n);
    printf("\n List is");
    display();
    reverse();
    printf("\n The list in reverse is: ");
    display();
}
void insert(int n)
{
    struct node *fnNode, *tmp;
    int num, i;
    stnode = (struct node *)malloc(sizeof(struct node));
        printf(" Enter data: ");
        scanf("%d", &num);
        stnode-> num = num;
        stnode-> link = NULL;
        tmp = stnode;
        for(i=2; i<=n; i++)
        {
            fnNode = (struct node *)malloc(sizeof(struct node));
                scanf(" %d", &num);
                fnNode->num = num;
                fnNode->link = NULL;
                tmp->link = fnNode;
                tmp = tmp->link;

        }
}
void reverse()
{
    struct node *prevNode, *curNode;
 if(stnode != NULL)
    {
        prevNode = stnode;
        curNode = stnode->link;
        stnode = stnode->link;

        prevNode->link = NULL;
        while(stnode != NULL)
        {
            stnode = stnode->link;
            curNode->link = prevNode;

            prevNode = curNode;
            curNode = stnode;
        }
        stnode = prevNode;
    }
}

void display()
{
    struct node *tmp;
    if(stnode == NULL)
    {
        printf(" No data found in the list.");
    }
    else
    {
        tmp = stnode;
        while(tmp != NULL)
        {
            printf(" Data = %d\n", tmp->num);
            tmp = tmp->link;
        }
    }
}
