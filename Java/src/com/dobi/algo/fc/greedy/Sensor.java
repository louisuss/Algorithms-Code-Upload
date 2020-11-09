package com.dobi.algo.fc.greedy;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Sensor {
    public static int n, k;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        int[] positions = new int[n];
        for (int i = 0; i < n; i++) {
            positions[i] = sc.nextInt();
        }

        // 없으면 런타임 에러
        if (k >= n) {
            System.out.print(0);
            return;
        }

        Arrays.sort(positions);
        Integer[] distances = new Integer[n-1];
        for (int i = 1; i < n; i++) {
            distances[i-1] = positions[i] - positions[i-1];
        }

        Arrays.sort(distances, Collections.reverseOrder());
        for (int i = 0; i < k-1; i++) {
            distances[i] = 0;
        }
        int result = 0;
        for (int distance : distances) {
            result += distance;
        }
        System.out.print(result);
    }
}
