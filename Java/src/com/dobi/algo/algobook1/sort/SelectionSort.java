package com.dobi.algo.algobook1.sort;

public class SelectionSort {
    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7,5,3,1,4,10,9,8, 11,12};
        for (int i=0; i <n; i++) {
            int min_idx = i;
            for (int j = i+1; j < n; j++) {
                if (arr[min_idx] > arr[j]) {
                    min_idx = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }
}
