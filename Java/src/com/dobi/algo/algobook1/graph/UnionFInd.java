package com.dobi.algo.algobook1.graph;

import java.util.Scanner;

public class UnionFInd {
    public static int v, e;
    public static int[] parent = new int[1000001];

    // 특정 원소가 속한 집합 찾기
    public static int findParent(int x) {
        if (x == parent[x]) return x;
        return findParent(parent[x]);
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

        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            unionParent(a, b);
        }

        for (int i = 1; i <= v; i++) {
            System.out.println(findParent(i) + " ");
        }
        System.out.println();
        for (int i = 1; i <= v; i++) {
            System.out.println(parent[i] + " ");
        }
        System.out.println();
    }
}
