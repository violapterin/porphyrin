#! /usr/bin/env python3

import os

import porphyrin as PORPHYRIN

RELATIVE_IN = "test-in"
RELATIVE_OUT = "test-out"
folder_this = os.path.dirname(__file__)
folder_in = os.path.join(folder_this, RELATIVE_IN)
folder_out = os.path.join(folder_this, RELATIVE_OUT)
PORPHYRIN.main.convert(folder_in, folder_out)
