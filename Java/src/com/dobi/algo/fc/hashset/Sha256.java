package com.dobi.algo.fc.hashset;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

// 10930
public class Sha256 {
    public static void main(String[] args) throws NoSuchAlgorithmException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String base = br.readLine();

        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hash = md.digest(base.getBytes("UTF-8"));
        StringBuffer result = new StringBuffer();

        for (int i = 0; i < hash.length; i++) {
            String hex = Integer.toHexString(0xff & hash[i]);
            result.append(hex);
        }
        System.out.println(result.toString());
    }
}
