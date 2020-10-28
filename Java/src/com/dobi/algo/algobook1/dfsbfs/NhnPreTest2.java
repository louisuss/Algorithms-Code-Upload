package com.dobi.algo.algobook1.dfsbfs;

import java.util.*;

class Main {
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static int counter = 0;
    public static ArrayList<Integer> result = new ArrayList<>();

    public static boolean dfs(int x, int y, int sizeOfMatrix, int[][] matrix) {
        if (x < 0 || x >= sizeOfMatrix || y < 0 || y >= sizeOfMatrix) {
            return false;
        }

        if (matrix[x][y] == 1) {
            matrix[x][y] = 0;
            counter += 1;

            for (int i=0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < sizeOfMatrix && ny >= 0 && ny < sizeOfMatrix) {
                    dfs(nx, ny, sizeOfMatrix, matrix);
                }
            }
            return true;
        }
        return false;
    }

    private static void solution(int sizeOfMatrix, int[][] matrix) {
        int sector = 0 ;
        for (int i = 0; i < sizeOfMatrix; i++) {
            for (int j = 0; j < sizeOfMatrix; j++) {
                if (dfs(i, j, sizeOfMatrix, matrix)) {
                    sector += 1;
                    result.add(counter);
                    counter = 0;
                }
            }
        }
        System.out.println(sector);
        Collections.sort(result);
        for (int i = 0; i < result.size(); i++) {
            if (i != result.size()-1) {
                System.out.print(result.get(i) + " ");
            } else {
                System.out.println(result.get(i));
            }

        }
    }

    private static class InputData {
        int sizeOfMatrix;
        int[][] matrix;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
            for (int i = 0; i < inputData.sizeOfMatrix; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.sizeOfMatrix; j++) {
                    inputData.matrix[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.sizeOfMatrix, inputData.matrix);
    }
}
