#! /usr/bin/env python3

import os

import porphyrin as PORPHYRIN

SUBFOLDER_IN = "test-in"
SUBFOLDER_OUT = "test-out"
folder_this = os.path.dirname(__file__)
folder_in = os.path.join(folder_this, SUBFOLDER_IN)
folder_out = os.path.join(folder_this, SUBFOLDER_OUT)
PORPHYRIN.main.convert(folder_in, folder_out)
