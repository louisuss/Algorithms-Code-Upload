package com.dobi.algo.algobook1.dfsbfs;

public class Recursive2 {
    public static int factIter(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= 1;
        }
        return result;
    }

    public static int factRecursive(int n) {
        if (n <= 1) return 1;
        return n * factRecursive(n-1);
    }

    public static void main(String[] args) {
        System.out.println(factIter(5));
        System.out.println(factRecursive(5));
    }
}
