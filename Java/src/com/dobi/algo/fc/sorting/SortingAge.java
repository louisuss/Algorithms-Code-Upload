package com.dobi.algo.fc.sorting;

import java.util.Arrays;
import java.util.Scanner;

class Person implements Comparable<Person>{
    private int age;
    private int personNumber;
    private String name;

    public Person(int age, int personNumber, String name) {
        this.age = age;
        this.personNumber = personNumber;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    @Override
    public int compareTo(Person o) {
        if (this.age == o.age) {
            return Integer.compare(this.personNumber, o.personNumber);
        }
        return Integer.compare(this.age, o.age);
    }
}

public class SortingAge {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Person[] people = new Person[n];
        for (int i = 0; i < n; i++) {
            people[i] = new Person(sc.nextInt(), i, sc.next());
        }
        Arrays.sort(people);
        for (int i = 0; i < n; i++) {
            System.out.println(people[i].getAge() + " " + people[i].getName());
        }

//        ArrayList<Node> data = new ArrayList<Node>();
//
//        for (int i = 0; i < n; i++) {
//            int x = sc.nextInt();
//            String y = sc.next();
//            data.add(new Node(x, y));
//        }
//
//        Collections.sort(data, new Comparator<Node>() {
//            @Override
//            public int compare(Node a, Node b) {
//                return Integer.compare(a.age, b.age);
//            }
//        });
    }
}
