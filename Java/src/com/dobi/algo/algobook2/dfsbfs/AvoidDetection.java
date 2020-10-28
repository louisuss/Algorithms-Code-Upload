package com.dobi.algo.algobook2.dfsbfs;

import java.util.*;

class Combination {
    private int n;
    private int r;
    private int[] now; // 현재 조합
    private ArrayList<ArrayList<Position>> result; // 모든 조합
    
    public Combination(int n, int r) {
        this.n = n; // 빈 공간 크기
        this.r = r; // 조합 갯수
        this.now = new int[r];
        this.result = new ArrayList<>();
    }
    
    public ArrayList<ArrayList<Position>> getResult() {
        return result;
    }

    // 매개 변수 ??
    public void combination(ArrayList<Position> arr, int depth, int index, int target) {
        if (depth == r) {
            ArrayList<Position> temp = new ArrayList<>();
            // 현재 생성된 조합 복사
            for (int i = 0; i < now.length; i++) {
                temp.add(arr.get(now[i]));
            }
            result.add(temp);
            return;
        }

        if (target == n) return;
        now[index] = target;
        combination(arr,depth+1, index+1, target+1);
        combination(arr, depth, index, target+1);
    }
    
}

class Position {
    private int x;
    private int y;
    public Position(int x, int y) {
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
public class AvoidDetection {
    public static int n; // 복도 크기
    public static char[][] board = new char[6][6]; // 복도 정보
    public static ArrayList<Position> teachers = new ArrayList<>();
    public static ArrayList<Position> spaces = new ArrayList<>();
    
    // 특정 방향으로 감시 진행 (발견: true, 실패, false)
    public static boolean watch(int x, int y, int direction) {
        // 왼쪽 방향으로 감시 
        if (direction == 0) {
            while (y >= 0) {
                if(board[x][y] == 'S') {
                    return true;
                }
                if (board[x][y] == 'O') {
                    return false;
                }
            }
            y -= 1;
        }
        // 오른쪽
        if (direction == 1) {
            while (y < n) {
                if (board[x][y] == 'S') {
                    return true;
                }
                if (board[x][y] == 'O') {
                    return false;
                }
                y += 1;
            }
        }
        // 위쪽
        if (direction == 2) {
            while (x >= 0) {
                if (board[x][y] == 'S') {
                    return true;
                }
                if (board[x][y] == 'O') {
                    return false;
                }
                x -= 1;
            }
        }
        // 아래
        if (direction == 3) {
            while (x < n) {
                if (board[x][y] == 'S') {
                    return true;
                }
                if (board[x][y] == 'O') {
                    return false;
                }
                x += 1;
            }
        }
        return false;
    }
    // 장애물 설치 이후, 한명이라도 학생이 감지되는지 검사 
    public static boolean process() {
        // 모든 선생의 위치 하나씩 확인 
        for (int i = 0; i < teachers.size(); i++) {
            int x = teachers.get(i).getX();
            int y = teachers.get(i).getY();

            // 4방향 검사
            for (int j = 0; j < 4; j++) {
                if (watch(x, y, j)) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = sc.next().charAt(0);
                if (board[i][j] == 'T') {
                    teachers.add(new Position(i, j));
                }
                if (board[i][j] == 'X') {
                    spaces.add(new Position(i, j));
                }
            }
        }
        // 빈 공간에서 3개를 뽑는 모든 조합 확인
        Combination comb = new Combination(spaces.size(), 3);
        // 빈 공간 배열을 통해 가능한 모든 조합 생성
        comb.combination(spaces, 0, 0, 0);
        ArrayList<ArrayList<Position>> spaceList = comb.getResult();

        // 학생이 한명도 감지되지 않도록 설치 가능한지 여부
        boolean found = false;
        for (int i = 0; i < spaceList.size(); i++) {
            // 조합에 해당하는 공간에 벽 설치
            for (int j = 0; j < spaceList.get(i).size(); j++) {
                int x = spaceList.get(i).get(j).getX();
                int y = spaceList.get(i).get(j).getY();
                board[x][y] = 'O';
            }
            // 학생이 한명도 감지 안된 경우
            if (!process()) {
                found = true;
                break;
            }

            // 설치 장애물 다시 없애기
            for (int j = 0; j < spaceList.get(i).size(); j++) {
                int x = spaceList.get(i).get(j).getX();
                int y = spaceList.get(i).get(j).getY();
                board[x][y] = 'X';
            }
        }
        if (found) System.out.println("YES");
        else System.out.println("NO");
    }
}
