package com.dobi.algo.fc.dfsbfs;

import java.util.*;

public class Virus {
    public static final int MAX = 101;
    public static int computer, connection;
    public static boolean[] visited;
    public static HashMap<Integer, ArrayList<Integer>> network = new HashMap<>();

    public static int bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);

        while (!q.isEmpty()) {
            int now = q.poll();
            visited[now] = true;

            for (Integer next : network.get(now)) {
                if (!visited[next]) {
                    q.add(next);
                }
            }
        }
        int cnt = 0;
        for (int i = 0; i <= computer; i++) {
            if (visited[i]) {
                cnt += 1;
            }
        }
        return cnt-1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        computer = sc.nextInt();
        connection = sc.nextInt();
        visited = new boolean[computer+1];

        for (int i = 1; i <= computer; i++) {
            network.put(i, new ArrayList<>());
        }

        for (int i = 0; i < connection; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            // Hashmap ArrayList 조합에서 해당 키값에 값 추가하기
            network.get(a).add(b);
            network.get(b).add(a);
        }
        System.out.println(bfs(1));

    }
}
