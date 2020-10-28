package com.dobi.algo.fc.search;

import java.util.Arrays;
import java.util.Scanner;

public class Antena {
    public static int n, c;
    public static int[] homeList;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        c = sc.nextInt();
        homeList = new int[n];
        for (int i = 0; i < n; i++) {
            homeList[i] = sc.nextInt();
        }

        Arrays.sort(homeList);

        int minDistance = homeList[1] - homeList[0];
        int maxDistance = homeList[homeList.length-1] - homeList[0];

        int result = 0;
        while (minDistance <= maxDistance) {
            int mid = (maxDistance + minDistance) / 2; // 임의 거리지정
            int cnt = 1;
            int value = homeList[0];

            // 설치하기
            for (int i = 1; i < n; i++) {
                if (homeList[i] >= value + mid) {
                    value = homeList[i];
                    cnt += 1;
                }
            }
            if (cnt >= c) {
                result = mid;
                minDistance = mid + 1;
            } else {
                maxDistance = mid - 1;
            }
        }
        System.out.println(result);
    }
}
