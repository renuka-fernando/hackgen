package main

import "fmt"

func main() {
	var q, h1, m1, h2, m2, k int

	for fmt.Scan(&q); q > 0; q-- {
		fmt.Scan(&h1, &m1, &h2, &m2, &k)
		answer := (h1+k-h2)*60 + m1 - m2
		fmt.Println(answer)
	}
}
