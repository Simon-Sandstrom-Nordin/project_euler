package main

import (
	"fmt" // ForMaT
)

func main() {

	square_number_result := square_number()
	fmt.Println(square_number_result)

	square_sum_result := square_sum()
	fmt.Println(square_sum_result)

	result_difference := difference(square_sum_result, square_number_result)
	fmt.Print(result_difference)

}

func square_number() int {
	square_number := 0
	for i := 1; i <= 100; i++ {
		square_number += i * i
	}

	return square_number
}

func square_sum() int {
	square_sum := 0
	for i := 1; i <= 100; i++ {
		square_sum += i
	}

	return square_sum * square_sum
}

func difference(square_sum_result int, square_number_result int) int {
	return square_sum_result - square_number_result
}
