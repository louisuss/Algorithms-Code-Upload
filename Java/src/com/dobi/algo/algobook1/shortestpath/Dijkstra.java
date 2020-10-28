package com.dobi.algo.algobook1.shortestpath;
import java.util.*;


class Node {
    private int index;
    private int distance;

    public Node(int index, int distance) {
        this.index = index;
        this.distance = distance;
    }
    public int getIndex() {
        return this.index;
    }
    public int getDistance() {
        return this.distance;
    }
}

public class Dijkstra {
    public static final int INF = (int)1e9;
    public static int n, m, start;

    // 인접리스트
    public static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    public static boolean[] visited = new boolean[100001];
    public static int[] d = new int[100001];

    public static int getSmallestNode() {
        int minValue = INF;
        int index = 0;
        for (int i = 1; i <= n; i++) {
            if (d[i] < minValue && !visited[i]) {
                minValue = d[i];
                index = i;
            }
        }
        return index;
    }

    public static void dijkstra(int start) {
        d[start] = 0;
        visited[start] = true;

        // start node 에 인접한 노드 초기화
        for (int i = 0; i < graph.get(start).size(); i++) {
            d[graph.get(start).get(i).getIndex()] = graph.get(start).get(i).getDistance();
        }

        for (int i = 0; i < n-1; i++) {
            int now = getSmallestNode();
            visited[now] = true;

            // 현재 노드와 연결된 다른 노드를 확인
            for (int j = 0; j < graph.get(now).size(); j++) {
                int cost = d[now] + graph.get(now).get(j).getDistance();
                // 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if (cost < d[graph.get(now).get(j).getIndex()]) {
                    d[graph.get(now).get(j).getIndex()] = cost;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        start = sc.nextInt();

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            // a번 노드에서 b번노드로 가는 비용 c
            graph.get(a).add(new Node(b,c));
        }
        Arrays.fill(d, INF);

        dijkstra(start);

        for (int i = 1; i <= n; i++) {
            if (d[i] == INF) {
                System.out.println("INF");
            } else {
                System.out.println(d[i]);
            }
        }
    }
}
