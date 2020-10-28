package com.dobi.algo.algobook1.sort;

public class QuickSort {
    public static void quickSort(int[] arr, int start, int end) {
        if (start >= end) return; // 원소가 1개인 경우 종료
        int pivot = start;
        int left = start + 1;
        int right = end;

        while (left <= right) {
            // pivot 보다 큰 데이터 찾을 때 까지 반복
            while (left <= end && arr[left] <= arr[pivot]) left++;
            // pivot 보다 작은 데이터 찾을 때 까지 반복
            while (right > start && arr[right] >= arr[pivot]) right--;

            // 엇갈린 경우 작은 데이터와 피벗 교체
            if (left > right) {
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            }
            // 엇갈리지 않은 경우 작은 데이터와 큰 데이터 교체
            else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }
        quickSort(arr, start, right-1);
        quickSort(arr, right+1, end);
    }
    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7,5,3,1,4,10,9,8, 11,12};

        quickSort(arr, 0, n-1);

        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }
}
