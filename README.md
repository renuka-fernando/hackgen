# HackGen: HackerRank Test Case Generator
[![Build Status](https://travis-ci.org/renuka-fernando/hackgen.svg?branch=master)](https://travis-ci.org/renuka-fernando/hackgen)
[![HitCount](http://hits.dwyl.io/renuka-fernando/hackgen.svg)](http://hits.dwyl.io/renuka-fernando/hackgen)

Generate test cases for your problem easily. Credits to @aashutoshrathi.

## Table of Contents

- [HackGen: HackerRank Test Case Generator](#hackgen-hackerrank-test-case-generator)
  - [Table of Contents](#table-of-contents)
  - [1. Installation in Python](#1-installation-in-python)
  - [2. Getting Started](#2-getting-started)
    - [2.1. Identify your Input Format and Constraints](#21-identify-your-input-format-and-constraints)
    - [2.2. Your Solution Algorithm](#22-your-solution-algorithm)
    - [2.3. Define Input Format](#23-define-input-format)
      - [2.3.1. Required Information for TestGenerator](#231-required-information-for-testgenerator)
    - [2.4. Find the Zipped Test Files](#24-find-the-zipped-test-files)
  - [3. License](#3-license)
  - [4. Contributions](#4-contributions)

## 1. Installation in Python
HackGen is on PyPI, so you can use pip to install it:
```bash
# bash
$ pip install hackgen
```
After installation, you can [get started!](#2-getting-started)

## 2. Getting Started

For the example lets take the simple problem "[Clock Delay](https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay)" as the problem you have created.

### 2.1. Identify your Input Format and Constraints

> #### Input Format
> - The first line contains ***q***, the number of queries.
> - Each query is described by two lines. The first line contains four space-separated integers ***h1, m1, h2, m2***. The second line contains a single integer ***k***.

> #### Constraints
> - 1 ≤ ***q*** ≤ 1000
> - 0 ≤ ***h1*** < 23
> - 0 ≤ ***h2*** < 24
> - 0 ≤ ***m1***, ***m2*** < 60
> - 1 ≤ ***k***
> - ***h1*** + ***k*** < 24
> - It is guaranteed that ***h1:m1*** is strictly before ***h2:m2***

### 2.2. Your Solution Algorithm

This can be python, java, c++, c file. If you need support other languages please update the `Language` class in the [language.py](hackgen/language.py) file.

1. Your solution [logic.py](examples/clockdelay/logic.py) file.

```py
q = int(input())

for i in range(q):
    h1, m1, h2, m2 = map(int, input().split())
    k = int(input())
    delay = (h1 + k - h2) * 60 + m1 - m2
    print(delay)
```

2. Your solution [Logic.java](examples/clockdelay/Logic.java) file.

```java
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
```

### 2.3. Define Input Format

Create a file [clockdelay.clock_delay.py](examples/clockdelay/clock_delay.py) in the same directory the [logic.py](examples/clockdelay/logic.py) file contains.

Create the class `ClockDelayInputFormat` extending [`hackgen.TestInputFormat`](python/hackgen/test_input_format.py) and overriding `inputs(difficult_level: int) -> None` method with constraints and input format identified in the second step.

You can introduce difficulty with using `difficult_level` value which is between 0 and 9 inclusively [0-9].

```py
import random

from hackgen import TestInputFormat, TestGenerator, Language


class ClockDelayInputFormat(TestInputFormat):
    """
    Input format of Clock Delay challenge.
    https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay
    """

    # difficulty levels with test file number
    # difficulty level is [0-9]
    __diff = [(5, 10), (10, 30), (50, 100), (100, 300), (100, 300),
              (300, 600), (600, 900), (800, 1000), (900, 1000), (950, 1000)]

    def inputs(self, difficult_level: int) -> None:
        q = random.randint(*self.__diff[difficult_level])  # number of test cases
        print(q)
        for n in range(q):
            # constraints for h1 m1 h2 m2 k
            h1 = random.randint(0, 23)
            m1 = random.randint(0, 60)
            h2 = random.randint(h1, 24)
            k = random.randint(h2 - h1 + 1 if h1 == h2 else h2 - h1, 24 - h1)
            m2 = random.randint(0, (m1 if h1 + k == h2 else 60))
            print(h1, m1, h2, m2)
            print(k)


# input format instance
input_format = ClockDelayInputFormat()

# try with Language.java('Logic') also
test_generator = TestGenerator(10, input_format, Language.python('logic'), "ClockDelay")
test_generator.run()
```

Create instance `inputFormat` of [`clockdelay.ClockDelayInputFormat`](examples/clockdelay/clock_delay.py) class. Create generator using `hackgen.TestGenerator` class with required information.

#### 2.3.1. Required Information for TestGenerator

- Number of Test Files Needs: ***10***
- Instance of TestInputFormat: ***ClockDelayInputFormat***
- Language of Solution File (python, java, c++, c) and File Name: ***python(logic)*** also try with ***java(Logic)***
- Name of the Problem: ***ClockDelay***

### 2.4. Find the Zipped Test Files

Execute the script [clock_delay.py](examples/clockdelay/clock_delay.py).

Run the following in a terminal.
```bash
$ cd examples/clockdelay/ && python clock_delay.py
```

See the file `${Name}-test-cases.zip` contains in the directory `examples/clockdelay/`.

## 3. License

HackerRank Test Case Generator is [MIT licensed](./LICENSE).

## 4. Contributions

Contributions are welcome! :)