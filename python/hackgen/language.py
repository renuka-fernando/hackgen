# Copyright (c) 2018 Renuka Fernando
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os


class Language:
    """
    Programming Language to compile and run the solution algorithm.
    """

    def __init__(self, run_string: str) -> None:
        self.__run_string = run_string

    def get_run_string(self) -> str:
        return self.__run_string

    @staticmethod
    def php(file_name: str = 'logic') -> 'Language':
        return Language('php %s.php' % file_name)

    @staticmethod
    def python(file_name: str = 'logic') -> 'Language':
        return Language('python %s.py' % file_name)

    @staticmethod
    def java(file_name: str = 'Logic') -> 'Language':
        os.system('javac %s.java' % file_name)
        return Language('java %s' % file_name)

    @staticmethod
    def cpp(file_name: str = 'Logic') -> 'Language':
        os.system('g++ -o %s %s.cpp' % (file_name, file_name))
        return Language('%s' % file_name)

    @staticmethod
    def c(file_name: str = 'Logic') -> 'Language':
        os.system('gcc -o %s %s.c' % (file_name, file_name))
        return Language('./%s' % file_name)

    @staticmethod
    def go(file_name: str = 'logic') -> 'Language':
        return Language('go run %s.go' % file_name)
