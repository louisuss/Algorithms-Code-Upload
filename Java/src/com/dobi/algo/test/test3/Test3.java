package com.dobi.algo.test.test3;

import java.util.Scanner;

//1
//2(BR2(G))1(B2(B(R)))

//1
//2(B(1(R)2(GBB)))
public class Test3 {
    public static int numOfOrder;
    public static String[] orderArr;

    // 숫자(문자) * (   )
    public static String repeater(String order) {
        String result = "";

        if (Character.isDigit(order.charAt(0))) {
            order = order.replaceAll("\\(", "");
            order = order.replaceAll("\\)", "");
            int front = order.charAt(0) - '0';
            String back = order.substring(1);

            for (int i = 0; i < front; i++) {
                result += back;
            }
        } else {
            int idx = order.indexOf("(");
            String front = order.substring(0, idx);
            String back = order.substring(idx+1, order.length()-1);
            for (int i = 0; i < back.length(); i++) {
                result += front + back.charAt(i);
            }
        }
        return result;
    }

    // 숫자 * 문자1개
    public static String mulNumber(String order) {
        String newString = "";

        for (int i = 0; i < order.length()-1; i++) {
            char now = order.charAt(i);
            char next = order.charAt(i+1);

            if (Character.isDigit(now) && Character.isAlphabetic(next)) {
                String str = order.substring(i, i+2);
                newString = order.substring(0,i) + repeater(str) + order.substring(i+2);
                order = newString;
            }
        }
        return order;
    }

    public static String translator(String order) {
        // 숫자*문자1개인 부분 모두 처리
        order = mulNumber(order);

        // ( 가 존재하면 반복
        while (order.contains("(")) {
            int startLetter;
            int start = 0, end = 0;

            // 처음 ( ) 매칭되는 인덱스 구하기
            for (int i = 0; i < order.length(); i++) {
                if (order.charAt(i) == '(') {
                    start = i;
                }
                if (order.charAt(i) == ')') {
                    end = i;
                    break;
                }
            }

            // startLetter BRA(ABC) 부분 필터링이 오래걸림.
            startLetter = start - 1;

            // 문자가 2개 이상 처리되야되는 경우
            if (startLetter > 0) {
                startLetter -= 1;
                while (Character.isAlphabetic(order.charAt(startLetter))) {
                    if (startLetter == 0) break;
                    startLetter -= 1;
                }
            }

            // ( 나 ) 인 상태이기 때문에 하나 앞으로 이동
            if (startLetter != 0) {
                startLetter += 1;
            }

            System.out.println(start + ", " + startLetter);
            String str = repeater(order.substring(startLetter, end+1));
            order = order.substring(0, startLetter) + str + order.substring(end+1);
            order = mulNumber(order);
            System.out.println(order);
        }
        return order;
    }

    private static void solution(int numOfOrder, String[] orderArr) {
        for (int i = 0; i < numOfOrder; i++) {
            System.out.println(translator(orderArr[i]));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        numOfOrder = sc.nextInt();
        orderArr = new String[numOfOrder];

        for (int i = 0; i < numOfOrder; i++) {
            orderArr[i] = sc.next();
        }
        solution(numOfOrder, orderArr);
    }
}
