# Copyright (c) 2018 Renuka Fernando
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
import shutil
import sys
import time
import zipfile


class TestInputFormat:
    """
    Input Format of the Algorithm of the solution
    """
    def inputs(self, difficult_level: int) -> None:
        """
        Override this method with the input format.
        Generate inputs from random and print the values to be
        :param difficult_level: [0-9] use this value to adjust difficulty with test file number.
        :return: None
        """
        raise NotImplementedError("Input Format is Not Given")


class Language:
    """
    Programming Language to compile and run the solution algorithm.
    """

    def __init__(self, run_string: str) -> None:
        self.__run_string = run_string

    def get_run_string(self) -> str:
        return self.__run_string

    @staticmethod
    def python(file_name: str = 'Logic') -> 'Language':
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


class TestGenerator:
    """
    Test case generator.
    """

    def __init__(self, test_file_count: int, test_input_format: TestInputFormat, language: Language, name: str) -> None:
        if not isinstance(test_input_format, TestInputFormat):
            raise TypeError("`test_input_format` should be an instance of TestInputFormat")
        if not isinstance(language, Language):
            raise TypeError("`language` should be an instance of Language")
        self.__test_file_count = test_file_count
        self.__test_input_format = test_input_format
        self.__language = language
        self.__name = name

    @staticmethod
    def __create_folders() -> None:
        try:
            os.mkdir('input')
            os.mkdir('output')
        except OSError:
            pass

    def __generate_input_test_files(self) -> None:
        print('Generating Inputs', file=sys.stderr)
        for i in range(0, self.__test_file_count):
            print('Generating Input File:', i, file=sys.stderr)
            sys.stdout = open('input/input%02d.txt' % i, 'w')
            self.__test_input_format.inputs(int(i * 10 / (self.__test_file_count + 1)))
            sys.stdout.close()

    def __generate_output_test_files(self) -> None:
        print('Generating Outputs', file=sys.stderr)
        with zipfile.ZipFile('%s-test-cases.zip' % self.__name, 'w', zipfile.ZIP_DEFLATED) as zf:
            for i in range(0, self.__test_file_count):
                print('Generating Output File:', i, file=sys.stderr)
                start = time.time()
                os.system(self.__language.get_run_string() + ' < input/input%02d.txt > output/output%02d.txt' % (i, i))
                end = time.time()
                print('Time taken to execute Test File %02d: %02f seconds' % (i, end - start), file=sys.stderr)
                zf.write('input/input%02d.txt' % i)
                zf.write('output/output%02d.txt' % i)

    def run(self) -> None:
        """
        Generate test cases with generating inputs according to input format and get outputs from feeding these inputs
        to the compiled solution algorithm. Generate zipped file of test cases.
        :return: None
        """
        TestGenerator.__create_folders()
        self.__generate_input_test_files()
        self.__generate_output_test_files()
        shutil.rmtree('input')
        shutil.rmtree('output')
