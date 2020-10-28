package com.dobi.algo.algobook2.sort;

import java.util.*;

public class CardSort {
    public static int result;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<Integer> cards = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            cards.offer(sc.nextInt());
        }

        while (cards.size() != 1) {
            int card1 = cards.poll();
            int card2 = cards.poll();
            int sumCards = card1 + card2;
            result += sumCards;
            cards.offer(sumCards);
        }
        System.out.println(result);
    }
}
