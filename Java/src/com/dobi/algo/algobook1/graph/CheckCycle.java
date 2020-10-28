package com.dobi.algo.algobook1.graph;

import java.util.Scanner;

public class CheckCycle {
    public static int v, e;
    public static int[] parent = new int[100001];

    public static int findParent(int x) {
        if (x == parent[x]) return x;
        return parent[x] = findParent(parent[x]);
    }

    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        v= sc.nextInt();
        e = sc.nextInt();

        for (int i = 1; i <= v; i++) {
            parent[i] = i;
        }
        boolean cycle = false;

        for (int i = 1; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (findParent(a) == findParent(b)) {
                cycle = true;
                break;
            } else {
                unionParent(a, b);
            }
        }
        if (cycle) {
            System.out.println("Happened");
        } else {
            System.out.println("Not happened");
        }
    }
}
