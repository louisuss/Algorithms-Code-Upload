package com.dobi.algo.algobook1.graph;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Edge2 implements Comparable<Edge2> {
    private int distance;
    private int nodeA;
    private int nodeB;

    public Edge2(int distance, int nodeA, int nodeB) {
        this.distance = distance;
        this.nodeA = nodeA;
        this.nodeB = nodeB;
    }

    public int getDistance() {
        return distance;
    }

    public int getNodeB() {
        return nodeB;
    }

    public int getNodeA() {
        return nodeA;
    }

    @Override
    public int compareTo(Edge2 o) {
        if (this.distance < o.distance) {
            return -1;
        }
        return 1;
    }
}
public class KruscalQuestion {
    public static int v, e;
    public static int[] parent = new int[100001];
    public static ArrayList<Edge2> edges = new ArrayList<>();
    public static int result = 0;

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

        for (int i = 1; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int cost = sc.nextInt();
            edges.add(new Edge2(cost, a, b));
        }

        Collections.sort(edges);
        int last = 0; // 최소 신장 트리에 포함된 간선 중에서 가장 비용이 큰 간선

        for (int i = 0; i < edges.size(); i++) {
            int cost = edges.get(i).getDistance();
            int a = edges.get(i).getNodeA();
            int b = edges.get(i).getNodeB();
            if (findParent(a) != findParent(b)) {
                unionParent(a, b);
                result += cost;
                last = cost;
            }
        }
        System.out.println(result - last);
    }
}
