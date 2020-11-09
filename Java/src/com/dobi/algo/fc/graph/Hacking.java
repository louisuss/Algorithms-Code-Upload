package com.dobi.algo.fc.graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

class Computer implements Comparable<Computer>{
    private int next;
    private int time;

    public Computer(int next, int time) {
        this.next = next;
        this.time = time;
    }

    public int getNext() {
        return next;
    }

    public int getTime() {
        return time;
    }

    @Override
    public int compareTo(Computer o) {
        return this.time - o.time;
    }
}

public class Hacking {
    public static final int MAX = (int)1e9;
    public static int t;
    public static int n, d, c;
    public static ArrayList<ArrayList<Computer>> arr;
    public static int[] times;
    public static ArrayList<String> result = new ArrayList<>();

    public static void dijkstra(int start) {
        PriorityQueue<Computer> q = new PriorityQueue<>();
        q.offer(new Computer(start, 0));
        times[start] = 0;

        while (!q.isEmpty()) {
            Computer computer = q.poll();
            int now = computer.getNext();
            int time = computer.getTime();
            if (times[now] < time) {
                continue;
            }
            for (Computer c : arr.get(now)) {
                int updateTime = time + c.getTime();
                if (times[c.getNext()] > updateTime) {
                    times[c.getNext()] = updateTime;
                    q.offer(c);
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            n = sc.nextInt();
            d = sc.nextInt();
            c = sc.nextInt();

            arr = new ArrayList<>();

            times = new int[n+1];
            Arrays.fill(times, MAX);

            for (int j = 0; j <= n; j++) {
                arr.add(new ArrayList<>());
            }

            for (int j = 0; j < d; j++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                int s = sc.nextInt();

                arr.get(b).add(new Computer(a, s));
            }
            dijkstra(c);

            int cnt = 0;
            int maxTime = 0;
            for (int time : times) {
                if (time != MAX) {
                    cnt += 1;
                    maxTime = Math.max(maxTime, time);
                }
            }
            result.add(cnt + " " + maxTime);
        }
        for (String s : result) {
            System.out.println(s);
        }
    }
}
