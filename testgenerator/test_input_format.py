# Copyright (c) 2018 Renuka Fernando
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


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
