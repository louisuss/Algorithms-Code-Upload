package com.dobi.algo.algobook1.bs;

import java.util.Arrays;
import java.util.Scanner;

public class BinarySearchRecur {
    public static int binarySearch(int[] arr, int target, int start, int end) {
        if (start > end) return -1;
        int mid = (start+end)/2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] > target) return binarySearch(arr, target, start, mid-1);
        else return binarySearch(arr, target, mid+1, end);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int target = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);

        int result = binarySearch(arr, target,0, n-1);
        if (result == -1) {
            System.out.println("None");
        } else {
            System.out.println(result + 1);
        }
    }
}
