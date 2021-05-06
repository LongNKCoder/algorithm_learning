#include <iostream>
#include <stdio.h>
using namespace std;


void bubble_sort(int mang[], int phan_tu);

void bubble_sort(int mang[], int phan_tu){
    for(int i = 0; i<phan_tu-1; i++){
        for(int j = phan_tu-1; j>i; j--){
            if (mang[j] < mang[j-1]){
                int tmp;
                tmp = mang[j];
                mang[j] = mang[j-1];
                mang[j-1] = tmp;
            }
        }
    }
}

int main(){
    int mang[10] = {3, 5, 6, 1, 2, 0, 8, 9, 4, 7};
    bubble_sort(mang, 10);
    for(int i = 0; i<10; i++){
        cout << mang[i];
    }
    return 0;
}
