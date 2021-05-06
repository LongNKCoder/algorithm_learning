package main

import (
	"fmt"
)

func bubble_sort(mang []int) {
	phan_tu:= len(mang)
	for i := 0; i < phan_tu-1; i++ {
		for j := phan_tu - 1; j > i; j-- {
			if mang[j] < mang[j-1]{
				mang[j], mang[j-1] = mang[j-1],mang[j]
			}
		}
	}
}

func main() {
	mang := []int{3, 5, 6, 1, 2, 0, 8, 9, 4, 7}
	bubble_sort(mang)
	fmt.Println(mang)
}
