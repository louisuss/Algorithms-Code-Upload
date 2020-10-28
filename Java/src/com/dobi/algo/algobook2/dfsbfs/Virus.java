package com.dobi.algo.algobook2.dfsbfs;

import java.util.Scanner;
//7 7
//        2 0 0 0 1 1 0
//        0 0 1 0 1 2 0
//        0 1 1 0 1 0 0
//        0 1 0 0 0 0 0
//        0 0 0 0 0 1 1
//        0 1 0 0 0 0 0
//        0 1 0 0 0 0 0
public class Virus {
    public static int n, m, result = 0;
    public static int[][] map = new int[8][8];
    public static int[][] resultMap = new int [8][8];

    public static int[] dx = {-1, 0, 1, 0};
    public static int[] dy = {0, 1, 0, -1};

    public static void spreadVirus(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (resultMap[nx][ny] == 0) {
                    resultMap[nx][ny] = 2;
                    spreadVirus(nx, ny);
                }
            }
        }
    }

    public static int getScore() {
        int score = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (resultMap[i][j] == 0) {
                    score += 1;
                }
            }
        }
        return score;
    }

    // 울타리 설치하면서 매번 안전 영역 크기 계싼
    public static void dfs(int count) {
        // 설치 완료
        if (count == 3) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    resultMap[i][j] = map[i][j]; // 벽 설치한 맵 복사
                }
            }
            // 각 바이러스의 위치에서 전파 진행
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (resultMap[i][j] == 2) {
                        spreadVirus(i, j);
                    }
                }
            }
            // 안전 영역의 최대값 계산
            result = Math.max(result, getScore());
            return; // return 없으면 종료 안됨
        }
        // 빈 공간에 울타리 설치 - 모든 경우의 수
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {
                    map[i][j] = 1;
                    count += 1;
                    dfs(count);
                    map[i][j] = 0;
                    count -= 1;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                map[i][j] = sc.nextInt();
            }
        }
        dfs(0);
        System.out.println(result);
    }
}
