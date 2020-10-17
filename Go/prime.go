package main

import (
    "fmt"
    "math"
)


func isPrime(num int) bool {
    for i := 2; i <= int(math.Floor(math.Sqrt(float64(num)))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return value > 1
}




func main(){    
    var n int
    fmt.Print("Enter number to check prime: ")
    fmt.Scan(&n)   
    fmt.Print("number is prime: ",isPrime(n))
}
