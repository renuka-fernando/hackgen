# Copyright (c) 2018 Renuka Fernando
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from example.clockdelay.ClockDelayInputFormat import ClockDelayInputFormat
from testgenerator.TestGenerator import TestGenerator, Language


def generate_clock_delay():
    # input format instance
    input_format = ClockDelayInputFormat()

    # try with Language.java('Logic') also
    test_generator = TestGenerator(10, input_format, Language.python('Logic'), "ClockDelay")
    test_generator.run()


generate_clock_delay()
