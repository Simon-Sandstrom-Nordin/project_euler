package main

import (
	"fmt"
	"strconv"
)

func main() {

	for d := 1; d < 1000; d++ {
		var x float64 = 1 / float64(d)
		// fmt.Println(x)
		length := cycle_length(x)
		fmt.Println(length)
	}

}

func cycle_length(number float64) float64 {

	var length float64 = 0

	number_string := strconv.FormatFloat(number, 'f', 18, 64)
	number_string = number_string[2:len(number_string)]
	temp_string := ""

	for i := 0; i < len(number_string); i++ {
		temp_string += number_string[i : i+1]
	}

	return length

}

// I abandoned my dreams of completing this in Go.
// ... since they show up in different lengths.
// Onwards to MATLAB <3
