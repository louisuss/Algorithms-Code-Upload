package com.dobi.algo.fc.dfsbfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


// 백준 - 런타임 에러, but 실행잘됨...
public class HideSeek {
    public static final int MAX = 100001;
    public static int[] time = new int[MAX];

    public static int bfs(int n, int k) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(n);
        while (!q.isEmpty()) {
            int now = q.poll();

            if (now == k) {
                return time[now];
            }

            ArrayList<Integer> possible = new ArrayList<>();
            possible.add(now-1);
            possible.add(now+1);
            possible.add(now*2);

            for (int moved: possible) {
                if (time[moved] == 0 && 0 <= moved && moved < MAX) {
                    time[moved] = time[now]+1;
                    q.add(moved);
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        System.out.println(bfs(n, k));
    }
}
