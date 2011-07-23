# -*- coding: utf-8 -*-
#
#  Copyright 2011 Sybren A. Stüvel <sybren@stuvel.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

'''Functions for generating random numbers.'''

import math
import os

from rsa import common, transform

def read_random_int(nbits):
    """Reads a random integer of approximately nbits bits.
    
    The number of bits is rounded down to whole bytes to ensure that the
    resulting number can be stored in ``nbits`` bits.
    """

    randomdata = os.urandom(nbits // 8)
    return transform.bytes2int(randomdata)

def randint(maxvalue):
    """Returns a random integer x with 1 <= x <= maxvalue"""

    bit_size = common.bit_size(maxvalue)
    readbits = max(bit_size, 32)
    mask = (1 << bit_size) - 1

    while True:
        value = read_random_int(readbits) & mask
        if value <= maxvalue:
            return value

