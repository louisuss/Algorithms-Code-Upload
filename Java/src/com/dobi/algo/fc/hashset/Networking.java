package com.dobi.algo.fc.hashset;

import java.util.HashMap;
import java.util.Scanner;

public class Networking {
    public static int t, f;

    public static String find(HashMap<String, String> parent, String x) {
        if (parent.get(x) == x) {
            return x;
        } else {
            String p = find(parent, parent.get(x));
            parent.replace(x, p);
            return parent.get(x);
        }
    }

    public static void union(HashMap<String, String> parent, HashMap<String, Integer> number, String x, String y) {
        x = find(parent, x);
        y = find(parent, y);
        if (x != y) {
            parent.replace(y, x);
            number.replace(x, number.get(x)+number.get(y));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            HashMap<String, String> parent = new HashMap<>();
            HashMap<String, Integer> number = new HashMap<>();
            f = sc.nextInt();
            for (int j = 0; j < f; j++) {
                String a = sc.next();
                String b = sc.next();
                if (!parent.containsKey(a)){
                    parent.put(a, a);
                    number.put(a, 1);
                }
                if (!parent.containsKey(b)) {
                    parent.put(b, b);
                    number.put(b, 1);
                }
                union(parent, number, a, b);
                System.out.println(number.get(find(parent, a)));
            }
        }
    }
}
