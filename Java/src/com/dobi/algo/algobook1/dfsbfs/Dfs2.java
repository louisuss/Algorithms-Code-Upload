package com.dobi.algo.algobook1.dfsbfs;

import java.util.*;

class Node {
    private int index;
    private int distance;

    // 복사
    public Node(Node n) {
        this(n.index, n.distance);
    }

    // 초기화
    public Node() {
        this(0,0);
    }

    public Node(int index, int distance) {
        this.index = index;
        this.distance = distance;
    }

    public void show() {
        System.out.print("(" + this.index + ", " + this.distance + ")");
    }
}

public class Dfs2 {
    // 행이 3개인 인접리스트 표현
    public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();

    public static void main(String[] args) {
        for (int i=0; i < 3; i++) {
            graph.add(new ArrayList<Node>());
        }
        graph.get(0).add(new Node(1, 7));
        graph.get(0).add(new Node(2,5));
        graph.get(1).add(new Node(0, 7));
        graph.get(2).add(new Node(0, 5));

        for (int i=0; i<3; i++) {
            for (int j=0; j < graph.get(i).size(); j++) {
                graph.get(i).get(j).show();
            }
        }
    }
}
