package com.dobi.algo.algobook1.dfsbfs;

import java.util.LinkedList;
import java.util.Queue;

public class Queue1 {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(1);
        queue.offer(1);
        queue.offer(1);
        queue.offer(1);
        queue.offer(1);

        while (!queue.isEmpty()) {
            System.out.println(queue.size());
            System.out.println(queue.poll());
        }
        System.out.println(queue.size());
        System.out.println(queue);
    }
}
