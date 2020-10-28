package com.dobi.algo.algobook1.dfsbfs;

import java.util.*;

class Node4 {
    private int x;
    private int y;

    public Node4(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}

//6
//0 1 1 0 0 0
//0 1 1 0 1 1
//0 0 0 0 1 1
//0 0 0 0 1 1
//1 1 0 0 1 0
//1 1 1 0 0 0
public class NhnPreTest {
    public static int n;
    public static int[][] arr = new int[11][11];
    public static int c = 0;
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {1, -1, 0, 0};
    public static boolean[][] visited = new boolean[11][11];

    public static boolean dfs(int x, int y) {
        if (x < 0 || x >= n || y < 0 || y >= n) {
            return false;
        }
        if (arr[x][y] != 1) {
            return false;
        }

        if (arr[x][y] == 1 && !visited[x][y]) {
            c += 1;
            visited[x][y] = true;

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (!visited[nx][ny] && arr[nx][ny] == 1) {
                        dfs(nx, ny);
                        // return true; 마지막 경우가 체크가 안되는 문제 발생.
                    }
                }
            }
            return true;
        }
        return false;
    }
//    public static boolean bfs(int x, int y) {
//        if (x < 0 || x >= n || y < 0 || y >= n) {
//            return false;
//        }
//
//        if (arr[x][y] == 1 && !visited[x][y]) {
//            Queue<Node4> q = new LinkedList<>();
//            q.offer(new Node4(x, y));
//
//            while (!q.isEmpty()) {
//                System.out.println(q.size());
//                Node4 node = q.poll();
//                x = node.getX();
//                y = node.getY();
//                arr[x][y] = 0;
//                visited[x][y] = true;
//                for (int i = 0; i < 4; i++) {
//                    int nx = x + dx[i];
//                    int ny = y + dy[i];
//
//                    if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
//                        if (arr[nx][ny] == 1 && !visited[nx][ny]) {
//                            q.offer(new Node4(nx, ny));
//                        }
//                    }
//                }
//            }
//            return true;
//        }
//        return false;
//    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String[] newLine = sc.nextLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(newLine[j]);
            }
        }
        for (int i = 0; i < visited.length; i++) {
            Arrays.fill(visited[i], false);
        }

        int result = 0;
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(i, j)) {
                    result += 1;
                    answer.add(c);
                    c = 0;
                }
            }
        }
        System.out.println(result);
        for (int i = 0; i < answer.size(); i++) {
            System.out.print(answer.get(i) + " ");
        }
    }
}
