using System;

namespace HeapSort
{

    //A Heap Sort implementation
    //Time Complexity: O(nlog(n))

    class Program
    {
        //heap sort is responsible for building the heap.

        static void heapSort(int [] arr, int n)
        {
            for (int i = n / 2 - 1; i >= 0; i--)
                heapify(arr, n, i);

            for (int i = n - 1; i >= 0; i--)
            {
                int temp = arr[0];
                arr[0] = arr[i];
                arr[i] = temp;
                heapify(arr, i, 0);
            }

        }

        static void heapify(int [] arr, int n, int i)
        {
            int largest = i, left = 2 * i + 1, right = 2 * i + 2;

            if (left < n && arr[left] > arr[largest])
                largest = left;
            if (right < n && arr[right] > arr[largest])
                largest = right;
            if(largest != i)
            {
                int swap = arr[i];
                arr[i] = arr[largest];
                arr[largest] = swap;
                heapify(arr, n, largest);
            }
        }

        static void Main(string[] args)
        {
            int[] arr = { 55, 25, 89, 34, 12, 19, 78, 95, 1, 100 };
            int n = 10;

            Console.WriteLine("Initial array is : ");

            for(int i=0; i<n; i++)
                Console.Write(arr[i] + " ");

            heapSort(arr, 10);

            Console.WriteLine("\nSorted Array is: ");

            for (int i = 0; i < n; i++)
                Console.Write(arr[i] + " ");
        }
    }
}
