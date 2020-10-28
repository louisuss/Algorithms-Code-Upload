package com.dobi.algo.algobook2.dfsbfs;

public class MakeBalance {
    // ( ) 개수 같으면 균형잡힌 괄호 문자열
    public int balancedIndex(String p) {
        int count = 0;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') count += 1;
            else count -=1;
            if (count == 0) return i;
        }
        return -1;
    }

    public boolean checkProper(String p) {
        int count = 0;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') count += 1;
            else {
                // 쌍이 맞지 않는 경우에 false 반환
                if (count == 0) {
                    return false;
                }
                count -= 1;
            }
        }
        return true; // 쌍이 맞는 경우
    }

    public String solution(String p) {
        // 1. 빈문자열 처리
        String answer = "";
        if (p.equals("")) return answer;

        // 2. u, v
        int idx = balancedIndex(p);
        String u = p.substring(0, idx + 1);
        String v = p.substring(idx + 1);

        // 3-1
        // 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
        if (checkProper(u)) {
            answer = u + solution(v);
        }
        // 4
        else {
            // 4-1
            answer = "(";
            // 4-2
            answer += solution(v);
            // 4-3
            answer += ")";
            // 4-4
            u = u.substring(1, u.length() - 1);
            String temp = "";
            for (int i = 0; i < u.length(); i++) {
                // 뒤집기
                if (u.charAt(i) == '(') temp += ")";
                else temp += "(";
            }
            // 뒤에 붙이기
            answer += temp;
        }
        return answer;
    }
}