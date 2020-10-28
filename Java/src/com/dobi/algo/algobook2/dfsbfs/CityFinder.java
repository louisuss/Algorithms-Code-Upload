package com.dobi.algo.algobook2.dfsbfs;

import java.util.*;

public class CityFinder {
    public static int n, m, k, x;
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    public static int[] distance = new int[300001];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        x = sc.nextInt();

        for (int i = 0; i < m; i++) {
            graph.add(new ArrayList<>());
        }
        Arrays.fill(distance, -1);

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);
        }
        distance[x] = 0;

        Queue<Integer> q = new LinkedList<>();
        q.offer(x);
        while (!q.isEmpty()) {
            int now = q.poll();
            for (int i = 0; i < graph.get(now).size(); i++) {
                int nextNode = graph.get(now).get(i);
                if (distance[nextNode] == -1) {
                    distance[nextNode] = distance[now]+1;
                }
            }
        }
        boolean check = false;
        for (int i = 1; i <= n; i++) {
            if (distance[i] == k) {
                System.out.println(i);
                check = true;
            }
        }
        if (!check) System.out.println(-1);
    }
}
