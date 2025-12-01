package main

import (
	"fmt"
	"os"
)

func main() {
	part_num := os.Args[1]
	if len(os.Args) > 3 {
		panic("wrong number of arguments\n Please enter the comand in this format ")

	}
	if part_num == "1" {
		part_1()
	} else if part_num == "2" {
		part_2()
	} else {
		fmt.Println("Please enter the correct part of the problem this format")
	}

}
