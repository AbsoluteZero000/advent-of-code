package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func part_2() {
	file_name := os.Args[2]
	file, err := os.Open(file_name)

	if err != nil {
		fmt.Print("Error in Opening file\n")
		fmt.Print(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	res := 0
	i := 0
	for scanner.Scan() {
		line := scanner.Text()
		first, last := -1, -1

		for _, val := range line {
			if unicode.IsDigit(val) {
				if first == -1 {
					first = int(val) - int('0')
				} else {
					last = int(val) - int('0')
				}
			}
		}

		fmt.Println(line)
		fmt.Println("line ", i, ": first = ", first, " last = ", last)
		i++
		if last != -1 {
			first = first*10 + last
		} else {
			first += first * 10
		}

		fmt.Println("sum of line ", i, " is ", first)
		res += first
	}

	fmt.Println(res)

}
