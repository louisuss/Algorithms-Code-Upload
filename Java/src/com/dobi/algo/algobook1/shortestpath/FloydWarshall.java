package com.dobi.algo.algobook1.shortestpath;

import java.util.Arrays;
import java.util.Scanner;

public class FloydWarshall {
    public static final int INF = (int)1e9;
    public static int n, m;
    public static int[][] graph = new int[501][501]; // 2차원 배열 선언

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < 501; i++) {
            Arrays.fill(graph[i], INF);
        }

        // 대각선 부분 0으로 초기화
        for (int i = 0; i <= n; i++) {
            graph[i][i] = 0;
        }

        // a -> b, 비용 c
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            graph[a][b] = c;
        }

        // i -> j vs i -> k -> j
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    graph[i][j] = Math.min(graph[i][j], graph[i][k]+graph[k][j]);
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (graph[i][j] == INF) {
                    System.out.println("INF");
                } else {
                    System.out.println(graph[i][j]);
                }
            }
            System.out.println();
        }
    }
}
