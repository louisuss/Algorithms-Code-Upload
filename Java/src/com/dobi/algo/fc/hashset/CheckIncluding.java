package com.dobi.algo.fc.hashset;

import java.util.HashSet;
import java.util.Scanner;

public class CheckIncluding {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashSet<Integer> n_set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            n_set.add(sc.nextInt());
        }
        int m = sc.nextInt();
        int[] m_list = new int[m];
        for (int i = 0; i < m; i++) {
            m_list[i] = sc.nextInt();
        }

        for (int i : m_list) {
            if (n_set.contains(i)) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}
