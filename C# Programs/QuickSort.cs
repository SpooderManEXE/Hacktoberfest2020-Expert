using System;

namespace QuickSort
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Quick sort algorithm");

            int[] array = new int[10] { 5, 1, 7, 10, 2, 6, 8, 3, 4, 9 };

            Console.WriteLine("Before sort:");
            for (int i = 0; i < array.Length; i++)
            {
                Console.WriteLine(array[i]);
            }

            QuickSort(array, 0, array.Length - 1);

            Console.WriteLine("After sort:");
            for (int i = 0; i < array.Length; i++)
            {
                Console.WriteLine(array[i]);
            }
        }

        private static void QuickSort(int[] array, int start, int end)
        {
            if (start < end)
            {
                int i = Partition(array, start, end);
                QuickSort(array, start, i - 1);
                QuickSort(array, i + 1, end);
            }
        }

        private static int Partition(int[] array, int start, int end)
        {
            int temp;
            int p = array[end];
            int i = start - 1;

            for (int j = start; j <= end - 1; j++)
            {
                if (array[j] <= p)
                {
                    i++;
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }

            temp = array[i + 1];
            array[i + 1] = array[end];
            array[end] = temp;

            return i + 1;
        }
    }
}
