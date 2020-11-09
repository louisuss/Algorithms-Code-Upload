package com.dobi.algo.fc.tree;

import java.util.HashMap;
import java.util.Scanner;

class Node {
    private char data;
    private char left_node;
    private char right_node;

    public Node(char data, char left_node, char right_node) {
        this.data = data;
        this.left_node = left_node;
        this.right_node = right_node;
    }

    public char getData() {
        return data;
    }

    public char getLeft_node() {
        return left_node;
    }

    public char getRight_node() {
        return right_node;
    }
}

public class TreeOrder {
    public static int n;
    public static HashMap<Character, Node> tree = new HashMap<>();

    public static void preOrder(Node node) {
        System.out.print(node.getData());
        if (node.getLeft_node() != '.') {
            preOrder(tree.get(node.getLeft_node()));
        }
        if (node.getRight_node() != '.') {
            preOrder(tree.get(node.getRight_node()));
        }
    }

    public static void inOrder(Node node) {
        if (node.getLeft_node() != '.') {
            inOrder(tree.get(node.getLeft_node()));
        }
        System.out.print(node.getData());
        if (node.getRight_node() != '.') {
            inOrder(tree.get(node.getRight_node()));
        }
    }


    public static void postOrder(Node node) {
        if (node.getLeft_node()!= '.') {
            postOrder(tree.get(node.getLeft_node()));
        }
        if (node.getRight_node() != '.') {
            postOrder(tree.get(node.getRight_node()));
        }
        System.out.print(node.getData());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            char data = sc.next().charAt(0);
            char left_node = sc.next().charAt(0);
            char right_node = sc.next().charAt(0);

            tree.put(data, new Node(data, left_node, right_node));
        }
        preOrder(tree.get('A'));
        System.out.println();
        inOrder(tree.get('A'));
        System.out.println();
        postOrder(tree.get('A'));
    }
}
