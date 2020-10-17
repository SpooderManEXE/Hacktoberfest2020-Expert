using System;

//A Merge Sort implementation
//Time Complexity: O(nlog(n))

public class MergeSort
{
    public static void Main(string[] args)
    {
        int[] array = { 5, 9, 2, 3, 6, -7 };
        Console.WriteLine("Unsorted: [{0}]", string.Join(", ", array));

        var sortedArr = MergeSort(array, 0, array.Length - 1);

        Console.WriteLine("Sorted (Merge Sort): [{0}]", string.Join(", ", sortedArr));
    }

    private static int[] MergeSort(int[] array, int start, int end)
    {
        if (start < end)
        {
            int middle = (end + start) / 2;
            int[] leftArr = MergeSort(array, start, middle);
            int[] rightArr = MergeSort(array, middle + 1, end);
            int[] mergedArr = MergeArray(leftArr, rightArr);
            return mergedArr;
        }
        return new int[] { array[start] };
    }

    private static int[] MergeArray(int[] leftArr, int[] rightArr)
    {
        int[] mergedArr = new int[leftArr.Length + rightArr.Length];

        int leftIndex = 0;
        int rightIndex = 0;
        int mergedIndex = 0;

        // Traverse both arrays simultaneously and store the smallest element of both to mergedArr
        while (leftIndex < leftArr.Length && rightIndex < rightArr.Length)
        {
            if (leftArr[leftIndex] < rightArr[rightIndex])
            {
                mergedArr[mergedIndex++] = leftArr[leftIndex++];
            }
            else
            {
                mergedArr[mergedIndex++] = rightArr[rightIndex++];
            }
        }

        // If any elements remain in the left array, append them to mergedArr
        while (leftIndex < leftArr.Length)
        {
            mergedArr[mergedIndex++] = leftArr[leftIndex++];
        }

        // If any elements remain in the right array, append them to mergedArr
        while (rightIndex < rightArr.Length)
        {
            mergedArr[mergedIndex++] = rightArr[rightIndex++];
        }

        return mergedArr;
    }
}