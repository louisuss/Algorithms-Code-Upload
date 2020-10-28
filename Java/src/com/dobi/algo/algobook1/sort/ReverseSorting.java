package com.dobi.algo.algobook1.sort;

import java.util.*;

public class ReverseSorting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Integer[] arr = new Integer[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // 기본 정렬 라이브러리 이용해서 역순으로 정렬
        Arrays.sort(arr, Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }
}
