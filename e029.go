package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	var int_list []int

	for a := 2; a <= 100; a++ {
		for b := 2; b <= 100; b++ {
			var contains bool
			number := powers(a, b)
			for c := 0; c < len(int_list); c++ {
				if int_list[c] == number {
					contains = true
				}
			}
			if contains == false {
				int_list = append(int_list, number)
			}
		}
	}
	sort.Ints(int_list)
	fmt.Println(len(int_list))

}

func powers(a, b int) int {
	a_float := float64(a)
	b_float := float64(b)
	return int(math.Pow(a_float, b_float))
}
