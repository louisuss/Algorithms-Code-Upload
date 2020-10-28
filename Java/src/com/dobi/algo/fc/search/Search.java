package com.dobi.algo.fc.search;

import java.util.Scanner;

public class Search {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String word = sc.nextLine();

        int idx = 0;
        int result = 0;
        while (s.length()-idx >= word.length()) {
            // String 비교시 == 대신 equals 사용해야함
            if (s.substring(idx, idx+word.length()).equals(word)) {
                idx += word.length();
                result += 1;
            } else {
                idx += 1;
            }
        }
        System.out.println(result);
    }
}
