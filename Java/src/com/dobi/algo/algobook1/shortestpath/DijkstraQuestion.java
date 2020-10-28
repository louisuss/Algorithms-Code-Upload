package com.dobi.algo.algobook1.shortestpath;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

class Node3 implements Comparable<Node> {
    private int idx;
    private int distance;

    public Node3(int idx, int distance) {
        this.distance = distance;
        this.idx = idx;
    }

    public int getIdx() {
        return idx;
    }

    public int getDistance() {
        return distance;
    }

    @Override
    public int compareTo(Node other) {
        if (this.distance < other.getDistance()) {
            return -1;
        }
        return 1;
    }
}

public class DijkstraQuestion {
    public static final int INF = (int)1e9;
    public static int n, m, start;
    public static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    public static int[] d = new int[300001];

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        d[start] = 0;

        while(!pq.isEmpty()) {
            Node node = pq.poll();
            int dist = node.getDistance();
            int now = node.getIndex();

            if (d[now] < dist) continue;

            for (int i = 0; i < graph.get(now).size(); i++) {
                int cost = d[now] + graph.get(now).get(i).getDistance();
                if (cost < d[graph.get(now).get(i).getIndex()]) {
                    d[graph.get(now).get(i).getIndex()] = cost;
                    pq.offer(new Node(graph.get(now).get(i).getIndex(), cost));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        start = sc.nextInt();

        // 그래프 초기화
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Node>());
        }

        // 모든 간선 정보를 입력받기
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            // X번 노드에서 Y번 노드로 가는 비용이 Z라는 의미
            graph.get(x).add(new Node(y, z));
        }
        Arrays.fill(d, INF);

        dijkstra(start);

        int cnt = 0;
        int maxDistance = 0;
        for (int i = 1; i <= n; i++) {
            if (d[i] != INF) {
                cnt += 1;
                maxDistance = Math.max(maxDistance, d[i]);
            }
        }
        System.out.println(cnt-1 + " " + maxDistance);
    }
}
