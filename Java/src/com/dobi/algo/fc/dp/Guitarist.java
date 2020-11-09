package com.dobi.algo.fc.dp;

import java.util.Scanner;

public class Guitarist {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int m = sc.nextInt();

        int[] gap = new int[n];
        for (int i = 0; i < n; i++) {
            gap[i] = sc.nextInt();
        }

        int[][] dp = new int[n+1][m+1];
        dp[0][s] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (dp[i-1][j] == 0) {
                    continue;
                }

                int up = j + gap[i-1];
                int down = j - gap[i-1];
                if (up <= m) {
                    dp[i][up] = 1;
                }
                if (down >= 0) {
                    dp[i][down] = 1;
                }
            }
        }
        int result = -1;
        for (int i = m; i >= 0; i--) {
            if (dp[n][i] == 1) {
                result = i;
                break;
            }
        }
        System.out.println(result);
    }
}
