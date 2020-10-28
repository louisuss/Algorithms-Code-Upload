package com.dobi.algo.algobook1.simulation;

import java.util.Scanner;

public class Simul3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String inputData = sc.nextLine();
        int row = inputData.charAt(1) - '0';
        int col = inputData.charAt(0) - 'a' + 1;

        int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2};
        int[] dy = {-1, -2, -2, -1, 1, 2, 2, 1};

        int result = 0;
        for (int i = 0; i < 8; i++) {
            int nextRow = row + dx[i];
            int nextCol = col + dy[i];
            if (nextRow >= 1 && nextRow <=8 && nextCol >= 1 && nextCol <= 8)
                result+=1;
        }
        System.out.println(result);
    }
}
