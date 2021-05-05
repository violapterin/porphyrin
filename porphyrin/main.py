#! /usr/bin/env python3

import os

import organ as ORGAN
import stem as STEM
import leaf as leaf
import caution as CAUTION

def make(folder_in, folder_out):
   EXTENSION = ".ppr"
   things_in = os.scandir(folder_in)
   for thing in things_in:
      name_in = thing.name
      if not thing.is_file():
         print("Warning: ", name_in, " is not a file.")
         continue
      if not name_in.endswith(EXTENSION):
         print("Warning: ", name_in, " does not end in \"", EXTENSION, '\"')
         continue
      name_out = os.path.join(folder_out, name_in)
      if os.path.isfile(name_out):
         time_in = thing.stat().st_ctime
         time_out = thing.stat().st_ctime
         if time_in < time_out:
            continue
      convert(name_in, name_out) 

def convert(name_in, name_out):
   handle_in = open(name_in, mode = 'r')
   source = handle_in.read()
   handle_in.close()
   document = STEM.Document({"source": source})
   document.parse()
   sink = document.write()
   handle_out = open(name_out, mode = 'w')
   handle_out.write(sink)
   handle_out.close()
