package com.dobi.algo.fc.dp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Brick implements Comparable<Brick> {
    private int number;
    private int width;
    private int height;
    private int weight;

    public Brick() {

    }

    public Brick(int number, int width, int height, int weight) {
        this.number = number;
        this.width = width;
        this.height = height;
        this.weight = weight;
    }

    public int getNumber() {
        return number;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public int getWeight() {
        return weight;
    }

    @Override
    public int compareTo(Brick o) {
        if (this.weight < o.weight) {
            return -1;
        }
        return 1;
    }
}

public class StackBricks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Brick[] arr = new Brick[n+1];
        arr[0] = new Brick();

        for (int i = 1; i <= n; i++) {
            int width = sc.nextInt();
            int height = sc.nextInt();
            int weight = sc.nextInt();

            arr[i] = new Brick(i, width, height, weight);
        }

        Arrays.sort(arr);

        int[] dp = new int[n+1];
        Arrays.fill(dp, 0);
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i].getWidth() > arr[j].getWidth()) {
                    dp[i] = Math.max(dp[i], dp[j]+arr[i].getHeight());
                }
            }
        }

        int maxValue = 0;
        for (int i = 1; i <= n; i++) {
            maxValue = Math.max(maxValue, dp[i]);
        }
        int idx = n;
        ArrayList<Integer> result = new ArrayList<>();
        while (idx != 0) {
            if (maxValue == dp[idx]) {
                result.add(arr[idx].getNumber());
                maxValue -= arr[idx].getHeight();
            }
            idx -= 1;
        }
        Collections.reverse(result);
        System.out.println(result.size());
        for (Integer res : result) {
            System.out.println(res);
        }
    }
}
