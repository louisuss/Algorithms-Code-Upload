package com.dobi.algo.fc.backtracking;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// 에러
// 출력은 정답...
class Position {
    private int x;
    private int y;
    private String alpha;

    public Position(int x, int y, String alpha) {
        this.x = x;
        this.y = y;
        this.alpha = alpha;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String getAlpha() {
        return alpha;
    }
}
public class Alphabet {
    public static int r, c, result;
    public static String[][] field;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static boolean[][] visited;

    public static void bfs(int x, int y) {
        Queue<Position> q = new LinkedList<>();
        q.offer(new Position(x, y, field[x][y]));

        while (!q.isEmpty()) {
            Position position = q.poll();
            int localX = position.getX();
            int localY = position.getY();
            String step = position.getAlpha();
            visited[localX][localY] = true;
            result = Math.max(result, step.length());

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + localX;
                int ny = dy[i] + localY;
                if (0 <= nx && nx < r && 0 <= ny && ny <c && !visited[nx][ny]) {
                    if (!step.contains(field[nx][ny])) {
                        visited[nx][ny] = true;
                        q.offer(new Position(nx, ny, step.concat(field[nx][ny])));
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        r = sc.nextInt();
        c = sc.nextInt();
        field = new String[r][c];
        visited = new boolean[r][c];
        result = 0;

        for (int i = 0; i < r; i++) {
            String inputString = sc.next();
            for (int j = 0; j < inputString.length(); j++) {
                field[i][j] = Character.toString(inputString.charAt(j));
            }
        }
        bfs(0, 0);
        System.out.println(result);
    }
}
