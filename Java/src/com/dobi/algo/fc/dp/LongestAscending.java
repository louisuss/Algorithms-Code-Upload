package com.dobi.algo.fc.dp;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class LongestAscending {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        Integer[] dp = new Integer[n];
        Arrays.fill(dp, 1);

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
        }
        Arrays.sort(dp, Collections.reverseOrder());
        System.out.println(dp[0]);
    }
}
