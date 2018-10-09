import os
import shutil
import sys
import time
import zipfile


class TestInputFormat:
    def inputs(self, difficult_level: int):  # difficult level is in [0-9]
        raise NotImplementedError("Input Format is Not Given")


class Language:
    def __init__(self, run_string):
        self.run_string = run_string

    def get_run_string(self):
        return self.run_string

    @staticmethod
    def python(file_name='Logic'):
        return Language('python %s.py' % file_name)

    @staticmethod
    def java(file_name='Logic'):
        os.system('javac %s.java' % file_name)
        return Language('java %s' % file_name)

    @staticmethod
    def cpp(file_name='Logic'):
        os.system('g++ -o %s %s.cpp' % (file_name, file_name))
        return Language('%s' % file_name)

    @staticmethod
    def c(file_name='Logic'):
        os.system('gcc -o %s %s.c' % (file_name, file_name))
        return Language('./%s' % file_name)


class TestGenerator:

    def __init__(self, test_file_count: int, test_input_format: TestInputFormat, language: Language, name):
        if not isinstance(test_input_format, TestInputFormat):
            raise TypeError("`test_input_format` should be an instance of TestInputFormat")
        if not isinstance(language, Language):
            raise TypeError("`language` should be an instance of Language")
        self.test_file_count = test_file_count
        self.test_input_format = test_input_format
        self.language = language
        self.name = name

    @staticmethod
    def create_folders():
        try:
            os.mkdir('input')
            os.mkdir('output')
        except OSError:
            pass

    def generate_input_test_files(self):
        print('Generating Inputs', file=sys.stderr)
        for i in range(0, self.test_file_count):
            print('Generating Input File:', i, file=sys.stderr)
            sys.stdout = open('input/input%02d.txt' % i, 'w')
            self.test_input_format.inputs(int(i * 10 / (self.test_file_count + 1)))
            sys.stdout.close()

    def generate_output_test_files(self):
        print('Generating Outputs', file=sys.stderr)
        with zipfile.ZipFile('%s-test-cases.zip' % self.name, 'w', zipfile.ZIP_DEFLATED) as zf:
            for i in range(0, self.test_file_count):
                print('Generating Output File:', i, file=sys.stderr)
                start = time.time()
                os.system(self.language.get_run_string() + ' < input/input%02d.txt > output/output%02d.txt' % (i, i))
                end = time.time()
                print('Time taken to execute Test File %02d: %02f seconds' % (i, end - start), file=sys.stderr)
                zf.write('input/input%02d.txt' % i)
                zf.write('output/output%02d.txt' % i)

    def run(self):
        TestGenerator.create_folders()
        self.generate_input_test_files()
        self.generate_output_test_files()
        shutil.rmtree('input')
        shutil.rmtree('output')
