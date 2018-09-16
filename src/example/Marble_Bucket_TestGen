import random

from TestGenerator import TestGenerator
from TestGenerator import TestInputs


class MyProblem(TestInputs):
    def inputs(self):
        q = random.randint(1, 1000)  # constraints of value q
        print(q)
        for i in range(q):
            print(random.randint(1, 10000000))  # constraints of value x


test_inputs = MyProblem()
generator = TestGenerator(10, test_inputs)
generator.run()
