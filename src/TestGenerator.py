import os
import shutil
import sys
import time
import zipfile


class TestInputs:
    def inputs(self):
        raise NotImplementedError("Input Format is Not Given")


class Language:
    @staticmethod
    def python(file_name='Logic'):
        return 'python %s.py' % file_name

    @staticmethod
    def java(file_name='Logic'):
        os.system('javac %s.java' % file_name)
        return 'java %s' % file_name

    @staticmethod
    def cpp(file_name='Logic'):
        os.system('g++ -o %s %s.cpp' % file_name)
        return './%s' % file_name

    @staticmethod
    def c(file_name='Logic'):
        os.system('gcc -o %s %s.c' % file_name)
        return './%s' % file_name


class TestGenerator:

    def __init__(self, test_file_count, test_inputs, language, name):
        self.test_file_count = test_file_count
        self.test_inputs = test_inputs
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
        for i in range(0, self.test_file_count + 1):
            print('Generating Input File:', i, file=sys.stderr)
            sys.stdout = open('input/input%02d.txt' % i, 'w')
            self.test_inputs.inputs()
            sys.stdout.close()

    def generate_output_test_files(self):
        print('Generating Outputs', file=sys.stderr)
        with zipfile.ZipFile('%s-test-cases.zip' % self.name, 'w', zipfile.ZIP_DEFLATED) as zf:
            for i in range(0, self.test_file_count + 1):
                print('Generating Output File:', i, file=sys.stderr)
                start = time.time()
                os.system(self.language + ' < input/input%02d.txt > output/output%02d.txt' % (i, i))
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
