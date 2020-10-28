package com.dobi.algo.algobook1.sort;

import java.util.*;

public class BestSeller {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<String, Integer> books = new HashMap<>();
        ArrayList<String> result = new ArrayList<>();
        int max_value = 0;

        for (int i = 0; i < n; i++) {
            String book = sc.next();

            if (books.containsKey(book)) {
                books.put(book, books.get(book)+1);
            } else {
                books.put(book, 1);
            }
            max_value = Math.max(max_value, books.get(book));
        }

        for (String book : books.keySet()) {
            if (books.get(book) == max_value) result.add(book);
        }
        Collections.sort(result);
        System.out.println(result.get(0));

    }
}
