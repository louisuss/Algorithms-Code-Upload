package com.dobi.algo.fc.dfsbfs;

import java.util.ArrayList;
import java.util.Scanner;

public class Cabbage {
    public static int test;
    public static int m, n, k;
    public static int[][] arr;
    public static int[] dr = {-1,1,0,0};
    public static int[] dc = {0,0,-1,1};

    public static void dfs(int r, int c) {
        if (arr[r][c] == 1) {
            arr[r][c] = 0;
        }
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (0 <= nr && nr < n && 0 <= nc && nc <m) {
                if (arr[nr][nc] == 1) {
                    dfs(nr, nc);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        test = sc.nextInt();
        ArrayList<Integer> result = new ArrayList<>();

        for (int i = 0; i < test; i++) {
            m = sc.nextInt();
            n = sc.nextInt();
            k = sc.nextInt();
            arr = new int[n][m];
            for (int j = 0; j < k; j++) {
                int c = sc.nextInt();
                int r = sc.nextInt();
                arr[r][c] = 1;
            }
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                for (int l = 0; l < m; l++) {
                    if (arr[j][l] == 1) {
                        dfs(j, l);
                        cnt += 1;
                    }
                }
            }
            result.add(cnt);
        }

        for (Integer res : result) {
            System.out.println(res);
        }
    }
}
