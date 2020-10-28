package com.dobi.algo.algobook2.sort;

import java.util.*;

class Stage implements Comparable<Stage> {
    private int level;
    private double rate;

    public Stage(int level, double rate) {
        this.level = level;
        this.rate = rate;
    }

    public int getLevel() {
        return level;
    }


    @Override
    public int compareTo(Stage s) {
        if (this.rate == s.rate) {
            return Integer.compare(this.level, s.level);
        }
        return Double.compare(s.rate, this.rate);
    }
}
public class FailRate {
    public static void solution(int n, ArrayList<Integer> stages) {
        Collections.sort(stages);

        int leftPeople = stages.size(); // 남은 사람 숫자
        int idx = 0; // 위치
        ArrayList<Stage> result = new ArrayList<>(); // 결과 저장 리스트

        // level 1 ~ n
        for (int i = 1; i <= n; i++) {
            int failed = 0;
            for (int j = idx; j < stages.size(); j++) {
                if (i == stages.get(j)) {
                    failed += 1;
                }
                if (i < stages.get(j)) {
                    idx = j;
                    break;
                }
            }

            double failedRate = (double)failed / leftPeople;
            result.add(new Stage(i, failedRate));
            leftPeople -= failed;
        }

        Collections.sort(result);

        for (Stage stage : result) {
            System.out.println(stage.getLevel() + " ");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int number = sc.nextInt();
        ArrayList<Integer> stages = new ArrayList<>();
        for (int i = 0; i < number; i++) {
            stages.add(sc.nextInt());
        }

        solution(n, stages);
    }
}
