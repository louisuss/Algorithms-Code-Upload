package com.dobi.algo.algobook1.sort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Fruit implements Comparable<Fruit> {
    private String name;
    private int score;

    public Fruit(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return this.name;
    }

    public int getScore() {
        return this.score;
    }

    // 정렬 기준 점수가 낮은 순서
    @Override
    public int compareTo(Fruit other) {
        if (this.score < other.score) {
            return -1;
        }
        return 1;
    }
}
public class SortSettingOption {
    public static void main(String[] args) {
        List<Fruit> fruits = new ArrayList<>();

        fruits.add(new Fruit("banana", 2));
        fruits.add(new Fruit("apple", 5));
        fruits.add(new Fruit("graph", 3));

        Collections.sort(fruits);

        for (int i = 0; i < fruits.size(); i++) {
            System.out.println(fruits.get(i).getName()+", " + fruits.get(i).getScore());
        }

    }
}
