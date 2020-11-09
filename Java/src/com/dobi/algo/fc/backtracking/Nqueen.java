package com.dobi.algo.fc.backtracking;

import java.util.Arrays;
import java.util.Scanner;

public class Nqueen {
    public static int n;
    public static int[] row;
    public static int result = 0;

    public static boolean check(int x) {
        for (int i = 0; i < x; i++) {
            if (row[x] == row[i]) {
                return false;
            }
            if (Math.abs(row[x] - row[i]) == x - i) {
                return false;
            }
        }
        return true;
    }
    
    public static void dfs(int x) {
        if (x == n) {
            result += 1;
        } else {
            // x 행에 모든 열에 놓기
            for (int i = 0; i < n; i++) {
                row[x] = i;
                // 놓을 수 있는 위치인 경우 다음 경우 진행
                if (check(x)) {
                    dfs(x+1);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        row = new int[n];
        Arrays.fill(row, 0);
        dfs(0);
        System.out.println(result);
    }
}
