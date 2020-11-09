package com.dobi.algo.fc.dfsbfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Hacking {
    public static int n, m;
    public static HashMap<Integer, ArrayList<Integer>> network = new HashMap<>();
    public static StringBuffer result = new StringBuffer();

    public static int bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n+1];
        q.offer(start);
        int cnt = 1;

        while (!q.isEmpty()) {
            int now = q.poll();
            visited[now] = true;

            for (Integer next : network.get(now)) {
                if (!visited[next]) {
                    cnt += 1;
                    visited[next] = true;
                    q.offer(next);
                }
            }
        }

        return cnt;
    }

    public static void main(String[] args) throws IOException {
//        Scanner sc = new Scanner(System.in);
//        n = sc.nextInt();
//        m = sc.nextInt();
        // 시간 초과
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            network.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
//            int a = sc.nextInt();
//            int b = sc.nextInt();
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            network.get(b).add(a);
        }

        ArrayList<Integer> result = new ArrayList<>();
        int maxValue = 0;
        for (int i = 1; i <= n; i++) {
            int cnt = bfs(i);
            maxValue = Math.max(cnt, maxValue);
            result.add(cnt);
        }

        for (int i = 0; i < n; i++) {
            if (result.get(i) == maxValue) {
                System.out.print(i+1 + " ");
            }
        }

    }
}
