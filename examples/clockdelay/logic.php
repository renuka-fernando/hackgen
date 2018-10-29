<?php

# Copyright (c) 2018 Iordanis Fostiropoulos
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

$q = intval(readline());

for ($i = 0; $i < $q; $i++) {

    $input=explode(' ',readline());
    $h1 = $input[0];
    $m1 = $input[1];
    $h2 = $input[2];
    $m2 = $input[3];
    $k = intval(readline());
    $delay=($h1 + $k - $h2) * 60 + $m1 - $m2;
    echo $delay;
}

?>
