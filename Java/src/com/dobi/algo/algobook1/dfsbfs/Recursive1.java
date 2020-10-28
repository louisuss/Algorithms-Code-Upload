package com.dobi.algo.algobook1.dfsbfs;

public class Recursive1 {
    public static void recursiveFunc(int i) {
        if (i == 100) {
            return;
        }
        System.out.println(i + "Number");
        recursiveFunc(i+1);
    }

    public static void main(String[] args) {
        recursiveFunc(1);
    }
}
