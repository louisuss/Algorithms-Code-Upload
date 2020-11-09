package com.dobi.algo.fc.stackqueue;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class HeapQ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<Integer> q = new PriorityQueue<>();
        ArrayList<Integer> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int user_input = sc.nextInt();
            if (user_input == 0) {
                if (!q.isEmpty()) {
                    result.add(q.poll());
                } else {
                    result.add(0);
                }
            } else {
                q.offer(user_input);
            }
        }
        for (Integer res : result) {
            System.out.println(res);
        }
    }
}
