#include <stdio.h>

typedef struct
{
    int row;
    int col;
} Order;

typedef struct
{
    int row_i;
    int col_i;
    int val;
} Tuple;

void inputMatrix(int arr[][5], Order *order);
int convertToTuple(int arr[][5], Order *order, Tuple *tuple);
void printTuple(Tuple *tuple, int size);
int sumTuple(Tuple *tuple1, int size1, Tuple *tuple2, int size2, Tuple *res_tuple);
void printTranspose(Tuple *tuple, int tuple_sz);

int main()
{

    int a[5][5], b[5][5];
    Order mat_order;
    Tuple tuple_a[10], tuple_b[10], res_tuple[10];
    int tuple_size_a, tuple_size_b;

    printf("Enter the no:of rows in the matrix: ");
    scanf("%d", &mat_order.row);
    printf("Enter the no:of cols in the matrix: ");
    scanf("%d", &mat_order.col);

    printf("Enter the first matrix: \n");
    inputMatrix(a, &mat_order);

    printf("Enter the second matrix: \n");
    inputMatrix(b, &mat_order);

    tuple_size_a = convertToTuple(a, &mat_order, tuple_a);
    tuple_size_b = convertToTuple(b, &mat_order, tuple_b);

    printf("Tuple form of the two matrices are: \n");
    printTuple(tuple_a, tuple_size_a);
    printTuple(tuple_b, tuple_size_b);

    printf("Transposes of the two tuples are:\n");
    printTranspose(tuple_a, tuple_size_a);
    printTranspose(tuple_b, tuple_size_b);

    int res_size = sumTuple(tuple_a, tuple_size_a, tuple_b, tuple_size_b, res_tuple);

    printf("Sum of the two tuples are: \n");
    printTuple(res_tuple, res_size);

    return 0;
}

void inputMatrix(int arr[][5], Order *order)
{

    int *curr_elem_addr = 0;

    printf("Start entering: \n");
    for (int i = 0; i < order->row; i++)
    {
        for (int j = 0; j < order->col; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
}

/*
* Converts the matrix 'arr' into its tuple form.
* Stores the tuple form into 'tuple'
* returns the size of the tuple created
*/
int convertToTuple(int arr[][5], Order *order, Tuple *tuple)
{

    int tuple_index = 0;
    int curr_elem = 0;

    for (int i = 0; i < 10; i++)
        tuple[i].val = 0;

    for (int i = 0; i < order->row; i++)
    {
        for (int j = 0; j < order->col; j++)
        {
            if (arr[i][j] != 0)
            {
                tuple[tuple_index].row_i = i;
                tuple[tuple_index].col_i = j;
                tuple[tuple_index++].val = arr[i][j];
            }
        }
    }

    return tuple_index;
}

void printTuple(Tuple *tuple, int tuple_sz)
{

    printf("R     C      Value\n");
    for (int i = 0; i < tuple_sz; i++)
    {
        printf("%d     %d      %d\n",
               tuple[i].row_i,
               tuple[i].col_i,
               tuple[i].val);
    }
    printf("\n");
}
void printTranspose(Tuple *tuple, int tuple_sz)
{
    printf("R     C      Value\n");
    for (int i = 0; i < tuple_sz; i++)
    {
        printf("%d     %d      %d\n",
               tuple[i].col_i,
               tuple[i].row_i,
               tuple[i].val);
    }
    printf("\n");
}

int sumTuple(
    Tuple *tuple_a,
    int size_a,
    Tuple *tuple_b,
    int size_b,
    Tuple *res_tuple)
{
    int i_a = 0;
    int i_b = 0;
    int i_res = 0;

    while (i_a < size_a && i_b < size_b)
    {
        /* if a's row and col is smaller */
        if (
            tuple_a[i_a].row_i < tuple_b[i_b].row_i ||
            (tuple_a[i_a].row_i == tuple_b[i_b].row_i &&
             tuple_a[i_a].col_i < tuple_b[i_b].col_i))
        {
            res_tuple[i_res].row_i = tuple_a[i_a].row_i;
            res_tuple[i_res].col_i = tuple_a[i_a].col_i;
            res_tuple[i_res++].val = tuple_a[i_a++].val;
        }
        /* if b's row and col is smaller */
        else if (
            tuple_a[i_a].row_i > tuple_b[i_b].row_i ||
            (tuple_a[i_a].row_i == tuple_b[i_b].row_i &&
             tuple_a[i_a].col_i > tuple_b[i_b].col_i))
        {
            res_tuple[i_res].row_i = tuple_b[i_b].row_i;
            res_tuple[i_res].col_i = tuple_b[i_b].col_i;
            res_tuple[i_res++].val = tuple_b[i_b++].val;
        }
        else
        {
            res_tuple[i_res].row_i = tuple_b[i_b].row_i;
            res_tuple[i_res].col_i = tuple_b[i_b].col_i;

            int sum = (tuple_b[i_b++].val + tuple_a[i_a++].val);
            if (sum != 0)
            {
                res_tuple[i_res++].val = sum;
            }
        }
    }
    while (i_a < size_a)
    {
        res_tuple[i_res].row_i = tuple_a[i_a].row_i;
        res_tuple[i_res].col_i = tuple_a[i_a].col_i;
        res_tuple[i_res++].val = tuple_a[i_a++].val;
    }
    while (i_b < size_b)
    {
        res_tuple[i_res].row_i = tuple_b[i_b].row_i;
        res_tuple[i_res].col_i = tuple_b[i_b].col_i;
        res_tuple[i_res++].val = tuple_b[i_b++].val;
    }
    return i_res;
}
