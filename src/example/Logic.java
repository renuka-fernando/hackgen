/*
 * Copyright (c) 2018 Renuka Fernando
 * All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import java.util.Scanner;

public class Logic {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int q = scanner.nextInt();

        for (int i = 0; i < q; i++) {
            int h1, m1, h2, m2, k;
            h1 = scanner.nextInt();
            m1 = scanner.nextInt();
            h2 = scanner.nextInt();
            m2 = scanner.nextInt();
            k = scanner.nextInt();

            int delay = (h1 + k - h2) * 60 + m1 - m2;
            System.out.println(delay);
        }
    }
}