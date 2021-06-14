#! /usr/bin/env python3

import os

import porphyrin.aid as AID

subfolder_in = "test-cipher"
subfolder_out = "test-plain"
folder_this = os.path.dirname(__file__)
folder_in = os.path.join(folder_this, subfolder_in)
folder_out = os.path.join(folder_this, subfolder_out)
# # XXX comment out this line when debugging:
# AID.make_new(folder_in, folder_out)
# # XXX use this line when debugging:
AID.make_all(folder_in, folder_out)
