package com.dobi.algo.fc.sorting;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Point implements Comparable<Point>{
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getY() {
        return y;
    }

    public int getX() {
        return x;
    }

    @Override
    public int compareTo(Point p) {
        if (this.x == p.x) {
            return Integer.compare(this.y, p.y);
        }
        return Integer.compare(this.x, p.x);
    }
}
public class SortingPoint {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Point> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            points.add(new Point(x, y));
        }
        Collections.sort(points);
        for (Point point : points) {
            System.out.println(point.getX() + " " + point.getY());
        }
    }

}
