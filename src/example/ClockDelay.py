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
test_generator = TestGenerator(10, inputFormat, Language.java('Logic'), "ClockDelay")
test_generator.run()