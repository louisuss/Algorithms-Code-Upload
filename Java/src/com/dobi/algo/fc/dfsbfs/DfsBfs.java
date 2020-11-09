package com.dobi.algo.fc.dfsbfs;

import java.util.*;

public class DfsBfs {
    public static int n,m,v;
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    public static boolean[] visited = new boolean[1001];

    public static void dfs(int start) {
//        if (visited[start]) return;
        System.out.print(start + " ");
        visited[start] = true;

        for (Integer next : graph.get(start)) {
            if (!visited[next]) {
                dfs(next);
            }
        }
    }
//    public static void dfs(int x) {
//        if (visited[x]) return;
//        visited[x] = true;
//        System.out.print(x + " ");
//        for (int i = 0; i < graph.get(x).size(); i++) {
//            int y = graph.get(x).get(i);
//            dfs(y);
//        }
//    }

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);

        while (!q.isEmpty()) {
            int now = q.poll();
            if (!visited[now]) {
                visited[now] = true;
                System.out.print(now + " ");
                for (Integer next : graph.get(now)) {
                    if (!visited[next]) {
                        q.offer(next);
                    }
                }
            }
        }
    }
//    public static void bfs(int x) {
//        Queue<Integer> q = new LinkedList<>();
//        q.offer(x);
//        visited[x] = true;
//
//        while (!q.isEmpty()) {
//            int now = q.poll();
//            System.out.print(now + " ");
//            for (int i = 0; i < graph.get(now).size(); i++) {
//                int y = graph.get(now).get(i);
//                if (!visited[y]) {
//                    q.offer(y);
//                    visited[y] = true;
//                }
//            }
//        }
//    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        v = sc.nextInt();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        for (ArrayList<Integer> list : graph) {
            Collections.sort(list);
        }
//        for(int i = 1; i <= n; i++) {
//            Collections.sort(graph.get(i));
//        }

        dfs(v);
        System.out.println();
        visited = new boolean[1001];
        bfs(v);
    }
}
