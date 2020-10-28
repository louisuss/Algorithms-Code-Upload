package com.dobi.algo.algobook1.bs;

import java.util.Scanner;

public class SequantialSearch {
    public static int sequantialSearch(int n, String target, String[] arr) {
        for (int i = 0; i < n; i++) {
            if (arr[i].equals(target)) {
                return i+1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String target = sc.next();

        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next();
        }
        System.out.println(sequantialSearch(n, target, arr));
    }
}
