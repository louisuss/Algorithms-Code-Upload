package com.dobi.algo.fc.tree;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

class Node2 {
    private int parent = -1;
    private int number;
    private int leftNode;
    private int rightNode;
    
    public Node2(int number, int leftNode, int rightNode) {
        this.number = number;
        this.leftNode = leftNode;
        this.rightNode = rightNode;
    }

    public void setParent(int parent) {
        this.parent = parent;
    }

    public void setLeftNode(int leftNode) {
        this.leftNode = leftNode;
    }

    public void setRightNode(int rightNode) {
        this.rightNode = rightNode;
    }

    public int getParent() {
        return parent;
    }

    public int getleftNode() {
        return leftNode;
    }

    public int getrightNode() {
        return rightNode;
    }
}

public class TreeLevelWidth {
    public static int n, x, levelDepth;
    public static HashMap<Integer, Node2> tree = new HashMap<>();
    public static int[] minValue;
    public static int[] maxValue;
    
    public static void inOrder(Node2 node, int level) {
        levelDepth = Math.max(levelDepth, level);
        if (node.getleftNode() != -1) {
            inOrder(tree.get(node.getleftNode()), level+1);
        }
        minValue[level] = Math.min(minValue[level], x);
        maxValue[level] = Math.max(maxValue[level], x);
        x += 1;
        if (node.getrightNode() != -1) {
            inOrder(tree.get(node.getrightNode()), level+1);
        }
    }

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        n = sc.nextInt();
        x = 1; // 현재 진행중인 행 저장 변수
        levelDepth = 1;
        int root = -1;
        minValue = new int[n+1];
        maxValue = new int[n+1];
        Arrays.fill(minValue, n);
        Arrays.fill(maxValue, 0);

        // 트리 초기화
        for (int i = 1; i <= n; i++) {
            tree.put(i, new Node2(i, -1, -1));
        }

        for (int i = 1; i <= n; i++) {
            int number = sc.nextInt();
            int leftNode = sc.nextInt();
            int rightNode = sc.nextInt();

            tree.get(number).setLeftNode(leftNode);
            tree.get(number).setRightNode(rightNode);

            if (leftNode != -1) {
                tree.get(leftNode).setParent(number);
            }
            if (rightNode != -1) {
                tree.get(rightNode).setParent(number);
            }
        }

        for (int i = 1; i <= n; i++) {
            if (tree.get(i).getParent() == -1) {
                root = i;
            }
        }

        inOrder(tree.get(root), 1);
        int levelResult = 1;
        int widthResult = maxValue[1] - minValue[1] + 1;
        for (int i = 2; i <= n; i++) {
            int width = maxValue[i] - minValue[i] + 1;
            if (widthResult < width) {
                widthResult = width;
                levelResult = i;
            }
        }

        System.out.println(levelResult + " " + widthResult);
    }
}
