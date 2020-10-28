package com.dobi.algo.fc.search;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// 메모리 초과
class Bridge {
    private int next;
    private int weight;

    public Bridge(int next, int weight) {
        this.next = next;
        this.weight = weight;
    }

    public int getNext() {
        return next;
    }

    public int getWeight() {
        return weight;
    }
}

public class BridgeWeight {
    public static int n, m;
    public static ArrayList<ArrayList<Bridge>> adj = new ArrayList<>();
    public static int startFactory, finishFactory;

    public static boolean bfs(int weight) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(startFactory);
        boolean[] visited = new boolean[n+1];
        visited[startFactory] = true;

        while (!q.isEmpty()) {
            int a = q.poll();
            for (Bridge bridge : adj.get(a)) {
                // Boolean[] 선언 시 visited[]에서 오류 - Boolean[] 초기화 -> null  VS boolean[] 초기화 -> false
                if (!visited[bridge.getNext()] && bridge.getWeight() >= weight) {
                    visited[bridge.getNext()] = true;
                    q.offer(bridge.getNext());
                }
            }
        }
        return visited[finishFactory];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        int minWeight = (int)1e7;
        int maxWeight = 1;

        for (int i = 0; i < n+1; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int weight = sc.nextInt();
            adj.get(a).add(new Bridge(b, weight));
            adj.get(b).add(new Bridge(a, weight));
            minWeight = Math.min(minWeight, weight);
            maxWeight = Math.max(maxWeight, weight);
        }
        startFactory = sc.nextInt();
        finishFactory = sc.nextInt();

        int result = minWeight;
        while (minWeight <= maxWeight) {
            int mid = (minWeight + maxWeight) / 2;
            if (bfs(mid)) {
                result = mid;
                minWeight += 1;
            } else {
                maxWeight -= 1;
            }
        }
        System.out.println(result);
    }
}
