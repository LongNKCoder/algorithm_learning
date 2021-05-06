package main

import (
	"fmt"
)

func intercharge_sort(mang []int){
	phan_tu := len(mang)
	for i := 0; i < phan_tu; i++{
		for j := i + 1; j < phan_tu; j++{
			if mang[i] > mang[j]{
				mang[i], mang[j] = mang[j], mang[i]
			}
		}
	}
	return
}

func main(){
	mang := []int{3, 5, 6, 1, 2, 0, 8, 9, 4, 7}
	intercharge_sort(mang)
	fmt.Println(mang)
}
