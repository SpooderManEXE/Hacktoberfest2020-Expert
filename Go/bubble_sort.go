// This program outputs an ascendent ordered array
package main

import "fmt"

var size int

func bubble_sort(array []int) []int {
	swapped := true
	for swapped {
		swapped = false
		for i := 1; i < len(array); i++ {
			if array[i] < array[i-1] {
				array[i-1], array[i] = array[i], array[i-1]
				swapped = true
			}
		}
	}
	return array
}

func main() {
	fmt.Print("Enter the size of your array to be ordered: ")
	fmt.Scan(&size)
	array := make([]int, size)
	fmt.Println("Enter a sequence of integer numbers")
	for i := 0; i < size; i++ {
		fmt.Print("Enter a integer: ")
		fmt.Scan(&array[i])
	}
	fmt.Print("The ordered array is: ", bubble_sort(array))
}
