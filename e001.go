package main

import (
	"fmt" //ForMaT
)

func main() {
	fmt.Print("Enter integer:")
	var input_integer int
	fmt.Scan(&input_integer)
	var number int = check_multiplicity(input_integer)
	fmt.Println(number)

}

func check_multiplicity(a int) int {
	counter := 0
	for i := 1; i < a; i++ {
		if i%3 == 0 {
			counter += i
		} else if i%5 == 0 {
			counter += i
		}
	}

	return counter
}
