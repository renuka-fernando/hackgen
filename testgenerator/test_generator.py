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

from testgenerator.language import Language
from testgenerator.test_input_format import TestInputFormat


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
