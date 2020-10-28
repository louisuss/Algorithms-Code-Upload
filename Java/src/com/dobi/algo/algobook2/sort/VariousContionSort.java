package com.dobi.algo.algobook2.sort;

import java.util.*;

class Students implements Comparable<Students>{
    String name;
    int kor;
    int eng;
    int math;

    public Students(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    public String getName() {
        return name;
    }


    /*
    [ 정렬 기준 ]
    1) 두 번째 원소를 기준으로 내림차순 정렬
    2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
    3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
    4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
    */

    @Override
    public int compareTo(Students s) {
        if (this.kor == s.kor && this.eng == s.eng && this.math == s.math) {
            return this.name.compareTo(s.name);
        }
        // 감소하는 순서
        if (this.kor == s.kor && this.eng == s.eng) {
            return Integer.compare(s.math, this.math);
        }
        // 증가하는 순서
        if (this.kor == s.kor) {
            return Integer.compare(this.eng, s.eng);
        }
        return Integer.compare(s.kor, this.kor);
    }
}
public class VariousContionSort {
    public static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        ArrayList<Students> students = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String name = sc.next();
            int kor = sc.nextInt();
            int eng = sc.nextInt();
            int math = sc.nextInt();
            students.add(new Students(name, kor, eng, math));

//            String[] input = sc.nextLine().split(" ");
//            students.add(new Students(input[0], Integer.parseInt(input[1]), Integer.parseInt(input[2]), Integer.parseInt(input[3])));
        }

        Collections.sort(students);

        for (int i = 0; i < n; i++) {
            System.out.println(students.get(i).getName());
        }
    }
}
