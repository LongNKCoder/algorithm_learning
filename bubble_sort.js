function bubble_Sort(mang){
    var phan_tu = mang.length, i, j, tmp;
    for (i=0; i < phan_tu-1; i++){
        for (j=phan_tu-1; j > i; j--){
            if (mang[j] < mang[j-1]){
                tmp = mang[j]
                mang[j] = mang[j-1]
                mang[j-1] = tmp
            }
        }
    }
}
var mang;
mang = [3, 5, 6, 1, 2, 0, 8, 9, 4, 7];
bubble_Sort(mang)
console.log(mang);
