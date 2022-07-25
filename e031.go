package main

import "fmt"

func main() {

	counter := 0

	for a := 0; a <= 200; a++ { // 1 pence
		for b := 0; b <= 100; b++ { // 2 pence
			for c := 0; c <= 40; c++ { // 5 pence
				for d := 0; d <= 20; d++ { // 10 pence
					for e := 0; e <= 10; e++ { // 20 pence
						for f := 0; f <= 4; f++ { // 50 pence
							for g := 0; g <= 2; g++ { // 1 pound
								for h := 0; h <= 1; h++ {
									sum := a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200
									if sum == 200 {
										counter += 1
									}
								}
							}
						}
					}
				}
			}
		}
	}

	fmt.Println(counter)

}
