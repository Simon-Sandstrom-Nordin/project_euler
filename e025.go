package main

import (
	"fmt" // ForMaT
)

func main() {
	index_counter := 1
	f1 := 1
	f2 := 1
	var f_temp int
	searching := true
	for searching {
		index_counter += 1
		f_temp = fibonacci(f1, f2)
		f1 = f2
		f2 = f_temp
		f_string := f_temp
		if index_counter == 5 {
			searching = false
		}
	}

	fmt.Print(index_counter)
}

func fibonacci(first, second int) int {
	return first + second
}

// I just realized... this won't work in go.
// No data type can hold a 1000-digit number...
