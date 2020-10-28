package com.dobi.algo.fc.sorting;

import java.util.Scanner;


public class PrintDescend {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char[] c = s.toCharArray();
        for (int i = 9; i >= 0; i--) {
            for (char c1 : c) {
                if (i == (c1-'0')) {
                    System.out.print(i);
                }
            }
        }
        System.out.println();
//        for (int i = 9; i > 0; i--) {
//            for (int j = 0; j < s.length(); j++) {
//                if (s.charAt(j) -'0' == i) {
//                    System.out.print(i);
//                }
//            }
//        }
    }
}
