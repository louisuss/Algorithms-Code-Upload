package com.dobi.algo.algobook2.simulation;

public class CompressedString {
    public int solution(String s) {
        int answer = s.length();
        // 압축하는 단위 1 ~ 절반
        for (int step = 1; step < s.length()/2+1; step++) {
            String compressed = "";
            String prev = s.substring(0, step); // 앞에서 step만큼 문자열 추출
            int cnt = 1;

            // 단위만큼 증가시키며 이전 문자열과 비교
            for (int i = step; i < s.length(); i+=step) {
                // 이전 상태와 동일하다면 압축 횟수 증가
                // i ~ step 길이만큼 문자 생성
                String sub = "";
                for (int j = i; j < i + step; j++) {
                    if (j < s.length())
                        sub += s.charAt(j);
                }
                if (prev.equals(sub)) {
                    cnt += 1;
                } else { // 다른 문자열이 나와서 더 이상 압축 못하는 경우
                    // 숫자가 1이 아닌 경우 숫자 + 문자열 - 압축
                    compressed += (cnt >= 2) ? cnt + prev : prev;

                    // 진행된 부분 부터 다시 단위만큼 부분문자 생성
                    sub = "";
                    for (int j = i; j < j + step; j++) {
                        if (j < s.length())
                            sub += s.charAt(j);
                    }
                    prev = sub; // 다시 상태 초기화
                    cnt = 1;
                }
            }
            // 남아있는 문자열에 대해서 처리
            compressed += (cnt >= 2) ? cnt + prev : prev;
            answer = Math.min(answer, compressed.length());
        }
        return answer;
    }
}
