# HackerRank Test Case Generator
## Get Started
For the example lets take the simple problem "[Clock Delay](https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay)" as the problem have created.

### 01. Identify your Input Format and Constraints
> ### Input Format
> - The first line contains ***q***, the number of queries.
> - Each query is described by two lines. The first line contains four space-separated integers ***h1, m1, h2, m2***. The second line contains a single integer ***k***.

> ### Constraints
> - 1 ≤ ***q*** ≤ 1000
> - 0 ≤ ***h1*** < ***23***
> - 0 ≤ ***h2*** < 24
> - 0 ≤ ***m1***, ***m2*** < 60
> - 1 ≤ ***k***
> - ***h1*** + ***k*** < 24
> - It is guaranteed that ***h1:m1*** is strictly before ***h2:m2***

### 02. Your Solution Algorithm
Your solution [Logic.py](src/example/Logic.py) file. This can be python, java, c++, c file.
```py
q = int(input())

for i in range(q):
    h1, m1, h2, m2 = map(int, input().split())
    k = int(input())
    delay = (h1 + k - h2) * 60 + m1 - m2
    print(delay)
```

### 03. Test Generator File
Create a file [ClockDelay.py](src/example/ClockDelay.py) in the same directory the [Logic.py](src/example/Logic.py) file contains.

Create the class `ClockDelayInputFormat` extending `TestInputFormat` and overriding `inputs()` method with constraints and input format identified in the second step.
```py
import random

from TestGenerator import TestGenerator, TestInputFormat, Language


# Problem https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay
class ClockDelayInputFormat(TestInputFormat):
    def inputs(self):
        q = random.randint(10, 1000)  # number of test cases
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


inputFormat = ClockDelayInputFormat()
test_generator = TestGenerator(10, inputFormat, Language.python('Logic'), "ClockDelay")
test_generator.run()
```

Create instance `inputFormat` of `ClockDelayInputFormat` class. Craete generator using `TestGenerator` class with required information.

#### 03.1 Required Information for TestGenerator
- Number of Test Files Needs: ***10***
- Instance of TestInputFormat: ***ClockDelayInputFormat***
- Language of Solution File (python, java, c++, c) and File Name: ***python(Logic)***
- Name of the Problem: ***ClockDelay***

### 04. Find the Zipped Test Files
See the directory the [Logic.py](src/example/Logic.py) file contains with the name `${Name}-test-cases.zip`.