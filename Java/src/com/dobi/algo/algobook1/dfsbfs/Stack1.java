package com.dobi.algo.algobook1.dfsbfs;

import java.util.Stack;

public class Stack1 {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();

        stack.push("abc");
        stack.push("abc");
        stack.push("abc");
        stack.push("abc");
        stack.push("abc");
        stack.push("abc");

        while (!stack.isEmpty()) {
            System.out.println(stack.peek());
            stack.pop();
        }
        System.out.println(stack);
    }
}
