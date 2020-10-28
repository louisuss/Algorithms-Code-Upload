package com.dobi.algo.test.test1;

import java.util.ArrayList;
import java.util.Scanner;

//6
//2
//B C
//2
//3 -2

class Person {
    private char name;
    private int cnt;

    public Person(char name, int cnt) {
        this.name = name;
        this.cnt = cnt;
    }

    public char getName() {
        return name;
    }

    public int getCnt() {
        return cnt;
    }

    public void setCnt(int cnt) {
        this.cnt = cnt;
    }
}

public class Test1 {
    public static int startIdx;
    public static ArrayList<Person> players = new ArrayList<>();
    public static Person[] circle;

    public static int numOfAllplayers;
    public static int numOfQuickPlayer;
    public static String[] namesOfQuickPlayers;
    public static int numOfGames;
    public static int[] numOfMovesPerGame;


    public static void solution(int numOfAllPlayers, int numOfQuickPlayer, String[] namesOfQuickPlayers, int numOfGames, int[] numOfMovesPerGame) {
        startIdx = 0;

        // 플레이어 생성
        for (int i = 0; i < numOfAllPlayers; i++) {
            players.add(new Person((char) ((int) 'A' + i), 0));
        }

        // 술래 A 생성
        Person tagger = players.get(0);

        // 술래 기본 횟수 추가
        players.get(0).setCnt(1);

        // 앉은 위치 (B부터 차례대로 앉기)
        circle = new Person[numOfAllPlayers - 1];
        for (int i = 0; i < numOfAllPlayers-1; i++) {
            circle[i] = players.get(i+1);
        }

        // 게임 횟수 반복
        for (int game = 0; game < numOfGames; game++) {
            int move = numOfMovesPerGame[game]; // 이동 거리
            int put; // 수건 놓는 위치
            int oneCircle = numOfAllPlayers - 1; // 앉은 사람 인원
            boolean checkCatch = false; // 잡히는지 여부

            // 음수 방향(반시계방향)이 주어지면 양수(시계방향)로 바꿔서 계산
            if (move < 0) {
                move = -move + 1;
            }
            put = startIdx + move; // 손수건 놓는 위치
            if (put >= oneCircle) {
                put = put % oneCircle;
            }

            // 술래 교체 (손수건 놓은위치 사람이랑 술래랑 교체)
            Person temp = tagger;
            tagger = circle[put];
            circle[put] = temp;
            startIdx = put;

            // 술래가 빠른 경우 잡힘
            for (int i = 0; i < numOfQuickPlayer; i++) {
                if (tagger.getName() == namesOfQuickPlayers[i].charAt(0)) {
                    checkCatch = true;
                }
            }

            // 잡힌 경우 - 술래 교체 후 종료
            if (checkCatch) {
                temp = tagger;
                tagger = circle[put];
                circle[put] = temp;
                tagger.setCnt(tagger.getCnt() + 1); // 걸린 횟수 추가
            } else {
                tagger.setCnt(tagger.getCnt() + 1); // 걸린 횟수 추가
            }
        }

        for (int i = 0; i < circle.length; i++) {
            System.out.println(circle[i].getName() + " " + circle[i].getCnt());
        }
        System.out.println(tagger.getName() + " " + tagger.getCnt());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        numOfAllplayers = sc.nextInt();
        numOfQuickPlayer = sc.nextInt();
        namesOfQuickPlayers = new String[numOfQuickPlayer];
        for (int i = 0; i < numOfQuickPlayer; i++) {
            namesOfQuickPlayers[i] = sc.next();
        }
        numOfGames = sc.nextInt();
        numOfMovesPerGame = new int[numOfGames];
        for (int i = 0; i < numOfGames; i++) {
            numOfMovesPerGame[i] = sc.nextInt();
        }

        solution(numOfAllplayers, numOfQuickPlayer, namesOfQuickPlayers, numOfGames, numOfMovesPerGame);
    }
}