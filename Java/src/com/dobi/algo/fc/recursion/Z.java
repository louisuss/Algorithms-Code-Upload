package com.dobi.algo.fc.recursion;

import java.util.Scanner;


public class Z {
    public static int number=0;
    public static int n, target_r, target_c;

    // 반드시 재귀문은 return하거나 종료지점 필요함.
    public static void zFunc(int n, int r, int c) {
        if (n == 2) {
            if (r == target_r && c == target_c) {
                System.out.println(number);
                return;
            }
            number += 1;
            if (r == target_r && c+1 == target_c) {
                System.out.println(number);
                return;
            }
            number += 1;
            if (r+1 == target_r && c == target_c) {
                System.out.println(number);
                return;
            }
            number += 1;
            if (r+1 == target_r && c+1 == target_c) {
                System.out.println(number);
                return;
            }
            number += 1;
            return;
        }
        zFunc(n/2, r, c);
        zFunc(n/2, r, c+n/2);
        zFunc(n/2, r+n/2, c);
        zFunc(n/2, r+n/2, c+n/2);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        target_r = sc.nextInt();
        target_c = sc.nextInt();
        zFunc((int)Math.pow(2, n), 0, 0);
    }
}
