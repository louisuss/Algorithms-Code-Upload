package com.dobi.algo.fc.sorting;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class TopologySort {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        ArrayList<Integer> result = new ArrayList<>();
        int[] indegree = new int[n+1];

        for (int i = 0; i <= n; i++) {
            arr.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            arr.get(a).add(b);
            indegree[b] += 1;
        }
        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                heap.offer(i);
            }
        }
        while (!heap.isEmpty()) {
            int val = heap.poll();
            result.add(val);
            for (Integer b : arr.get(val)) {
                indegree[b] -= 1;
                if (indegree[b] == 0) {
                    heap.offer(b);
                }
            }
        }
        for (Integer val : result) {
            System.out.print(val + " ");
        }
    }
}
