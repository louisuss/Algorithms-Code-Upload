package com.dobi.algo.fc.graph;

import java.util.*;

// 메모리 초과
class Path implements Comparable<Path> {
    private int moved;
    private int cost;

    public Path(int moved, int cost) {
        this.moved = moved;
        this.cost = cost;
    }

    public int getMoved() {
        return moved;
    }

    public int getCost() {
        return cost;
    }


    @Override
    public int compareTo(Path o) {
        return this.cost - o.cost;
    }
}

public class AlmostShortestPath {
    public static final int MAX = (int)1e9;
    public static int n, m;
    public static int start, end;
    public static ArrayList<ArrayList<Path>> adj;
    public static ArrayList<ArrayList<Path>> reversedAdj;
    public static int[] distances;
    public static boolean[][] dropped;

    public static void dijkstra() {
        PriorityQueue<Path> q = new PriorityQueue<>();
        q.offer(new Path(start, 0));
        distances[start] = 0;

        while (!q.isEmpty()) {
            Path nowPath = q.poll();
            int now = nowPath.getMoved();
            int dist = nowPath.getCost();

            if (distances[now] < dist) {
                continue;
            }
            for (Path path : adj.get(now)) {
                int passedCost = path.getCost() + dist;
                if (passedCost < distances[path.getMoved()] && !dropped[now][path.getMoved()]) {
                    distances[path.getMoved()] = passedCost;
                    q.offer(new Path(path.getMoved(), passedCost));
                }
            }
        }
    }


    public static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        q.offer(end);
        while (!q.isEmpty()) {
            int now = q.poll();
            if (now == start) {
                continue;
            }
            for (Path path : reversedAdj.get(now)) {
                int prev = path.getMoved();
                int cost = path.getCost();
                if (distances[now] == distances[prev] + cost) {
                    dropped[prev][now] = true;
                    q.offer(prev);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            n = sc.nextInt();
            m = sc.nextInt();
            if (n == 0) {
                break;
            }
            start = sc.nextInt();
            end = sc.nextInt();

            // static 변수에서 초기화하는 경우 반복하는 동안 계속 한 객체로 실행하게되서 오류.
            adj = new ArrayList<>();
            reversedAdj = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                adj.add(new ArrayList<>());
            }

            for (int i = 0; i < n; i++) {
                reversedAdj.add(new ArrayList<>());
            }

            for (int i = 0; i < m; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int cost = sc.nextInt();
                adj.get(x).add(new Path(y, cost));
                reversedAdj.get(y).add(new Path(x, cost));
            }
            dropped = new boolean[n][n];
            distances = new int[n];
            Arrays.fill(distances, MAX);
            dijkstra();
            bfs();
            distances = new int[n];
            Arrays.fill(distances, MAX);
            dijkstra();

            if (distances[end] != MAX) {
                System.out.println(distances[end]);
            } else {
                System.out.println(-1);
            }
        }
    }
}
