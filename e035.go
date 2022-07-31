package main

import (
	"fmt"
	"strconv"
)

func main() {
	var counter int
	for k := 2; k < 1000000; k++ {
		if check_circular_primality(k) {
			counter += 1
		}
		if k%100 == 0 {
			fmt.Println(k)
		}
	}

	fmt.Print(counter)
}

func check_circular_primality(number int) bool {
	var length int
	string_number := strconv.Itoa(number)
	for k := 1; k <= len(string_number); k++ {
		length += 1
	}
	list := []int{}
	for j := 0; j < len(string_number); j++ {
		temp_string := ""
		counter := j
		for k := 0; k < len(string_number); k++ {
			temp_string = temp_string + string_number[counter:counter+1]
			counter += 1
			counter = counter % len(string_number)
		}
		temp_number, err := strconv.Atoi(temp_string)
		err = err // dumb but works, like my brother
		list = append(list, temp_number)
	}

	counter_prime := 0
	for k := 0; k < len(list); k++ {
		if isprime(list[k]) {
			counter_prime += 1
		}
	}

	// fmt.Println(list[0])
	// fmt.Println(isprime(list[0]))
	if len(list) == counter_prime {
		return true
	}
	return false
}

func isprime(number int) bool {
	for k := 2; k < number; k++ {
		if number%k == 0 {
			return false
		}
	}
	return true
}
