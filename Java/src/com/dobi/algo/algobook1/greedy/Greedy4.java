package com.dobi.algo.algobook1.greedy;

import java.util.Scanner;

public class Greedy4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;

        while (true) {
            // n = 28, k = 3 -> 27
            int target = (n/k) * k;
            // 28-27 만큼 +1
            result += (n-target);
            n = target;
            if (n<k) break;
            result += 1;
            n /= k;
        }
        result += (n-1);
        System.out.println(result);
    }
}
