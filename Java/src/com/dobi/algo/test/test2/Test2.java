package com.dobi.algo.test.test2;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

class Position {
    private int idx;
    private int siment;

    public Position(int idx, int siment) {
        this.idx = idx;
        this.siment = siment;
    }

    public int getIdx() {
        return idx;
    }

    public int getSiment() {
        return siment;
    }
}

public class Test2 {
    public static int[][] blocks;
    public static int day;
    public static int width;
    public static int volume;


    private static void caculateValue(int day, int width, int[][] blocks) {
        // 시멘트 누적
        for (int d = 0; d < day; d++) {
            if (d >= 1) {
                for (int i = 0; i < width; i++) {
                    blocks[d][i] += blocks[d - 1][i];
                }
            }

            ArrayList<Position> addPositions = new ArrayList<>();
            int left = 0;
            int right = width - 1;
            int leftMax = blocks[d][left];
            int rightMax = blocks[d][right];

            while (left < right) {
                // 이동하는 인덱스 위치가 더 큰경우 최대값이 이동한 값이됨. 그래서 added 값은 0 이거나 양수임.
                leftMax = Math.max(leftMax, blocks[d][left]);
                rightMax = Math.max(rightMax, blocks[d][right]);

                int added;
                if (leftMax <= rightMax) {
                    added = leftMax - blocks[d][left];
                    if (added != 0) {
                        addPositions.add(new Position(left, added));
                        volume += added;
                    }
                    left += 1;
                } else {
                    added = rightMax - blocks[d][right];
                    if (added != 0) {
                        addPositions.add(new Position(right, added));
                        volume += added;
                    }
                    right -= 1;
                }
            }

            for (int i = 0; i < addPositions.size(); i++) {
                int idx = addPositions.get(i).getIdx();
                int siment = addPositions.get(i).getSiment();

                blocks[d][idx] += siment;
            }
        }
        System.out.println(volume);
    }

    // 낮은 값 부터 채워나가기 -> 위 문제 풀이에 적합하지 않음
    public static void calculateVolume2(int day, int width, int[][] blocks) {
        for (int d = 0; d < day; d++) {
            if (d >= 1) {
                for (int i = 0; i < width; i++) {
                    blocks[d][i] += blocks[d-1][i];
                }
            }

            Stack<Integer> stack = new Stack<>();
            for (int i = 0; i < width; i++) {
                // 이전 값 보다 현재 값이 커지는 경우
                while (!stack.isEmpty() && blocks[d][i] > blocks[d][stack.peek()]) {
                    int top = stack.pop(); // 이전 인덱스

                    if (stack.isEmpty()) {
                        break;
                    }

                    // 5 2 1 3 -> 2, 3 사이 1 값을 채워서 2로 만듬 -> 5, 3 사이 2값을 3으로 만드는데 필요한1을 이전 거리에도 추가
                    int distance = i - stack.peek() - 1;
                    int siment = Math.min(blocks[d][i], blocks[d][stack.peek()]) - blocks[d][top]; // 양끝중 작은 값 - 중간값


                    volume += distance * siment;
                }
                stack.push(i);
            }
        }
        System.out.println(volume);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        day = sc.nextInt();
        width = sc.nextInt();
        blocks = new int[day][width];

        for (int i = 0; i < day; i++) {
            for (int j = 0; j < width; j++) {
                blocks[i][j] = sc.nextInt();
            }
        }

        caculateValue(day, width, blocks);
    }
}