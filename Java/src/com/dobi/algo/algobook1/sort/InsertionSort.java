package com.dobi.algo.algobook1.sort;

public class InsertionSort {
    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7,5,3,1,4,10,9,8, 11,12};

        for (int i = 1;i <n; i++) {
            for (int j= i; j>0; j--) {
                if (arr[j] < arr[j-1]) {
                    int temp = arr[j];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                } else {
                    break;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }
}
