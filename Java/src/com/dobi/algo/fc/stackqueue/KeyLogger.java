package com.dobi.algo.fc.stackqueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

// 5397
public class KeyLogger {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc;
        tc = Integer.parseInt(br.readLine());

        while (tc-- > 0) {
            String s;
            s = br.readLine();

            Stack<Character> left = new Stack<>();
            Stack<Character> right = new Stack<>();

            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '-') {
                    if (!left.isEmpty()) left.pop();
                }
                else if (s.charAt(i) == '<') {
                    if (!left.isEmpty()) {
                        right.push(left.pop());
                    }
                }
                else if (s.charAt(i) == '>') {
                    if (!right.isEmpty()) {
                        left.push(right.pop());
                    }
                } else {
                    left.push(s.charAt(i));
                }
            }
            StringBuilder result = new StringBuilder();
            while (!right.isEmpty()) {
                left.push(right.pop());
            }
            while (!left.isEmpty()) {
                result.append(left.pop());
            }
            System.out.println(result.toString());
            System.out.println(result.reverse().toString());
        }
    }
}
