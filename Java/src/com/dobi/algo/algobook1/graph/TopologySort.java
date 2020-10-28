package com.dobi.algo.algobook1.graph;

import java.util.*;

public class TopologySort {
    public static int v, e;
    public static int[] indegree = new int[100001];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

    public static void topologySort() {
        ArrayList<Integer> result = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();

        for (int i = 1; i <= v; i++) {
            if (indegree[i] == 0) {
                q.offer(i);
            }
        }

        while (!q.isEmpty()) {
            int now = q.poll();
            result.add(now);

            for (int i = 0; i < graph.get(now).size(); i++) {
                indegree[graph.get(now).get(i)] -= 1;
                if (indegree[graph.get(now).get(i)] == 0) {
                    q.offer(graph.get(now).get(i));
                }
            }
        }

        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        v = sc.nextInt();
        e = sc.nextInt();

        // 그래프 초기화
        for (int i = 0; i <= v; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // 방향 그래프의 모든 간선 정보를 입력 받기
        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b); // 정점 A에서 B로 이동 가능
            // 진입 차수를 1 증가
            indegree[b] += 1;
        }

        topologySort();
    }


}
