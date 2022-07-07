package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	content, err := os.ReadFile("e013_.txt")
	if err != nil {
		log.Fatal(err)
	}

	string_content := strings.Split(string(content), "\r\n")

	fmt.Println(len(string_content))

	number := 0
	for i := 0; i < len(string_content); i++ {
		integer, err := strconv.ParseInt(string_content[i][0:15], 10, 0)
		number += int(integer)
		if err != nil {
			log.Fatal(err)
		}
	}

	fmt.Println(number)
}

// learned to read from file in Go... yay <3.
