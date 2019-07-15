#include <iostream>
#include <vector>

using namespace std;

long long merge(vector<long long>& arr, long long start, long long mid, long long end) {
    long long leftPosition = start;
    long long rightPosition = mid + 1;

    vector<long long> mergedArray;
    long long leftIsBiggerCnt = 0;

    while (leftPosition <= mid || rightPosition <= end) {
        if (leftPosition > mid)
            mergedArray.push_back(arr[rightPosition++]);
        else if (rightPosition > end)
            mergedArray.push_back(arr[leftPosition++]);
        else if (arr[leftPosition] <= arr[rightPosition])
            mergedArray.push_back(arr[leftPosition++]);
        else {
            mergedArray.push_back(arr[rightPosition++]);
            leftIsBiggerCnt += mid - leftPosition + 1;
        }
    }

    for (int i = start; i <= end; i++)
        arr[i] = mergedArray[i - start];

    return leftIsBiggerCnt;
}

long long split(vector<long long>& arr, long long start, long long end){
    if (start == end)
        return 0;

    long long leftIsBiggerCnt = 0;

    long long mid = (start + end) / 2;

    leftIsBiggerCnt += split(arr, start, mid);
    leftIsBiggerCnt += split(arr, mid + 1, end);

    leftIsBiggerCnt += merge(arr, start, mid, end);

    return leftIsBiggerCnt;
}

long long mergeSort(vector<long long>& arr) {
    return split(arr, 0, arr.size() - 1);
}

int main(){
    long long arraySize;

    cin >> arraySize;

    vector<long long> arr;

    for (long long i = 0; i < arraySize; i++){
        long long val;
        cin >> val;

        arr.push_back(val);
    }

    long long cnt = mergeSort(arr);
    cout << cnt;
}
