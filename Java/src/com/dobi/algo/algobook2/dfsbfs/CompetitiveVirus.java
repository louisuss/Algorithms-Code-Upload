package com.dobi.algo.algobook2.dfsbfs;

import java.util.*;

class Viruses implements Comparable<Viruses>{
    private int index;
    private int time;
    private int x;
    private int y;

    public Viruses(int index, int time, int x, int y) {
        this.index = index;
        this.time = time;
        this.x = x;
        this.y = y;
    }

    public int getIndex() {
        return index;
    }

    public int getTime() {
        return time;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    // 오름차순
    @Override
    public int compareTo(Viruses v) {
        if (this.index < v.index) {
            return -1;
        }
        return 1;
    }
}

public class CompetitiveVirus {
    public static int n, k;
    public static int[][] map = new int[201][201];
    public static ArrayList<Viruses> viruses = new ArrayList<>();

    public static int[] dx = {-1, 0, 1, 0};
    public static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = sc.nextInt();

                // 바이러스 등록
                if (map[i][j] != 0) {
                    // 번호, 시간, 위치x, 위치y
                    viruses.add(new Viruses(map[i][j], 0, i, j));
                }
            }
        }
        Collections.sort(viruses);

        int targetS = sc.nextInt();
        int targetX = sc.nextInt();
        int targetY = sc.nextInt();

        // BFS

        Queue<Viruses> q = new LinkedList<>();
        // 바이러스 큐에 삽입
        for (int i = 0; i < viruses.size(); i++) {
            q.offer(viruses.get(i));
        }

        while (!q.isEmpty()) {
            Viruses virus = q.poll(); // 바이러스 한종류 꺼내기
            if (virus.getTime() == targetS) {
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = virus.getX() + dx[i];
                int ny = virus.getY() + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (map[nx][ny] == 0) {
                        map[nx][ny] = virus.getIndex();
                        q.offer(new Viruses(virus.getIndex(), virus.getTime() + 1, nx, ny));
                    }
                }
            }
        }
        System.out.println(map[targetX-1][targetY-1]);
    }
}
