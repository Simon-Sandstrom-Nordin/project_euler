package main

import (
	"fmt"
)

func main() {
	x := 5
	fmt.Println(factorial(x))
}

func factorial(x int) int {
	if x == 1 {
		return 1
	}
	return x * factorial(x-1)
}
