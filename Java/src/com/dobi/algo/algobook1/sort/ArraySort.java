package com.dobi.algo.algobook1.sort;

import java.util.Arrays;

public class ArraySort {
    public static void main(String[] args) {
        int n = 15;
        // 모든 원소의 값이 0보다 크거나 같다고 가정
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};

        Arrays.sort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }
}
