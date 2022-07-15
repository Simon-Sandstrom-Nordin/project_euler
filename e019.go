package main

import (
	"fmt"
)

func main() {
	day := 0     // Jan 1 1900 was a Monday, let day = 0 denote Monday.
	counter := 0 // Sundays on first of month

	for year := 1900; year < 2001; year++ {
		day, counter = month_31(day, counter)            // January
		day, counter = month_febuary(day, year, counter) // Febuary
		day, counter = month_31(day, counter)            // March
		day, counter = month_30(day, counter)            // April
		day, counter = month_31(day, counter)            // May
		day, counter = month_30(day, counter)            // June
		day, counter = month_31(day, counter)            // July
		day, counter = month_31(day, counter)            // August
		day, counter = month_30(day, counter)            // September
		day, counter = month_31(day, counter)            // October
		day, counter = month_30(day, counter)            // November
		day, counter = month_31(day, counter)            // December
		if year == 1900 {
			counter = 0 // Don't count year 1900
		}
	}

	fmt.Println(counter)
}

func month_30(day, counter int) (int, int) {
	if day == 0 {
		counter += 1
	}
	for i := 1; i <= 30; i++ {
		day += 1
		day = day % 7
	}

	return day, counter
}

func month_31(day, counter int) (int, int) {
	if day == 0 {
		counter += 1
	}
	for i := 1; i <= 31; i++ {
		day += 1
		day = day % 7
	}

	return day, counter
}

func month_febuary(day, year, counter int) (int, int) {
	if day == 0 {
		counter += 1
	}

	if year%4 == 0 && year%400 != 0 { // leap year, who-hoo!
		for i := 1; i <= 28+1; i++ {
			day += 1
			day = day % 7
		}
	} else { // normal year...
		for i := 1; i <= 28; i++ {
			day += 1
			day = day % 7
		}
	}

	return day, counter
}
