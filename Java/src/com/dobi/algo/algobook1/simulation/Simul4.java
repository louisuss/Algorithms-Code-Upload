package com.dobi.algo.algobook1.simulation;

import java.util.Scanner;

public class Simul4 {
    public static int n,m,x,y,direction;
    // 방문한 위치 저장 위한 맵 생성하여 0으로 초기화
    public static int[][] d = new int[50][50];
    // 전체 맵 정보
    public static int[][] arr = new int[50][50];

    public static int[] dx = {-1,0,1,0};
    public static int[] dy = {0,1,0,-1};

    public static void turn_left() {
        direction -= 1;
        if (direction == -1) direction = 3;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n =  sc.nextInt();
        m = sc.nextInt();

        x = sc.nextInt();
        y = sc.nextInt();
        direction = sc.nextInt();
        d[x][y] = 1; // 현재 좌표 방문 처리

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        int cnt = 1;
        int turn_time = 0;
        while (true) {
            turn_left();
            int nx = x + dx[direction];
            int ny = y + dy[direction];
            if (d[nx][ny] == 0 && arr[nx][ny] == 0) {
                d[nx][ny] = 1;
                x = nx;
                y = ny;
                cnt += 1;
                turn_time = 0;
                continue;
            } else {
                turn_time += 1;
            }
            if (turn_time == 4) {
                nx = x - dx[direction];
                ny = y - dy[direction];
                // 뒤로 갈 수 있으면 이동
                if (arr[nx][ny] == 0) {
                    x = nx;
                    y = ny;
                } else break;
                turn_time = 0;
            }
        }
        System.out.println(cnt);
    }
}
