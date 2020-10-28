package com.dobi.algo.algobook2.sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 시간초과 -> buffer 사용해서 받아야함
public class GetK {
//    public static int n, k;
//    public static ArrayList<Integer> arr = new ArrayList<>();
    public static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        ArrayList<Integer> data = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            data.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(data);
        System.out.println(data.get(k-1));
//        Scanner sc = new Scanner(System.in);
//        n = sc.nextInt();
//        k = sc.nextInt();

//        arr = new int[n];
//        for (int i = 0; i < n; i++) {
//            arr[i] = sc.nextInt();
//        }
//        Arrays.sort(arr);
//        System.out.println(arr[k-1]);

//        for (int i = 0; i < n; i++) {
//            arr.add(sc.nextInt());
//        }
//        Collections.sort(arr);
//        System.out.println(arr.get(k-1));
    }
}
