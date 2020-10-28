package com.dobi.algo.algobook1.sort;

import java.util.*;

class Student implements Comparable<Student> {
    private String name;
    private int score;

    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return this.name;
    }

    public int getScore() {
        return this.score;
    }

    @Override
    public int compareTo(Student o) {
        if (this.score < o.score) {
            return -1;
        }
        return 1;
    }
}
public class SortingSettingOption2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        List<Student> students = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String name = sc.next();
            int score = sc.nextInt();
            students.add(new Student(name, score));
        }

        Collections.sort(students);

        Collections.sort(students, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                if (o1.getScore() < o2.getScore()) {
                    return -1;
                } else if (o1.getScore() > o2.getScore()) {
                    return 1;
                } else {
                    return 0;
                }
            }
        });

        for (int i = 0; i < students.size(); i++) {
            System.out.println(students.get(i).getName());
        }
    }
}
