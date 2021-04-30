#! /usr/bin/env python3

import os

from porphyrin import *

directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".asm") or filename.endswith(".py"): 
         # print(os.path.join(directory, filename))
         continue
     else:
         continue


IN="test-in"
OUT="test-out"

for files in "${IN}":
   file_out = #XXX
   str_in = read(file)
   str_out = convert(str_in)
   file_out = convert()

