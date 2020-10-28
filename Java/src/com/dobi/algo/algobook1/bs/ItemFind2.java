package com.dobi.algo.algobook1.bs;

import java.util.Scanner;

// Coungting
public class ItemFind2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[1000001];
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            arr[x] = 1;
        }
        int m = sc.nextInt();
        int[] targets = new int[n];
        for (int i = 0; i < m; i++) {
            targets[i] = sc.nextInt();
        }

        for (int i = 0; i < m; i++) {
            if (arr[targets[i]] == 1) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
    }
}
