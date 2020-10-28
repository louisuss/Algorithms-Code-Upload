package com.dobi.algo.algobook1.dfsbfs;

import java.util.*;

class Node2 {
    private int index;
    private int distance;

    public Node2(int index, int distance) {
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

public class Bfs2 {
    public static int n, m;
    public static int[][] graph = new int[201][201];

    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static int bfs(int x, int y) {
        Queue<Node2> queue = new LinkedList<>();
        queue.offer(new Node2(x, y));

        while (!queue.isEmpty()) {
            Node2 node = queue.poll();
            x = node.getIndex();
            y = node.getDistance();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (graph[nx][ny] == 1) {
                        graph[nx][ny] = graph[x][y] + 1;
                        queue.offer(new Node2(nx, ny));
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.println(graph[i][j]);
            }
        }
        return graph[n-1][m-1];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = str.charAt(j) -'0';
            }
        }
        System.out.println(bfs(0,0));
    }
}
