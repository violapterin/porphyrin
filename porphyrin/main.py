#! /usr/bin/env python3

import os

import organ as ORGAN
import stem as STEM
import leaf as LEAF
import caution as CAUTION

def make(folder_in, folder_out):
   EXTENSION = ".ppr"
   things_in = os.scandir(folder_in)
   for thing_in in things_in:
      name_in = thing.name
      path_in = os.path.join(folder_in, name_in)
      if not thing_in.is_file():
         print("Warning: ", name_in, " is not a file.")
         continue
      if not path_in.endswith(EXTENSION):
         print("Warning: file ", name_in, " does not end in \"", EXTENSION, "\".")
         continue
      path_out = os.path.join(folder_out, path_in)
      if os.path.isfile(path_out):
         time_in = thing.stat().st_ctime
         time_out = os.path.getmtime(path_out)
         if time_in < time_out:
            continue
      convert(path_in, path_out) 

def convert(path_in, path_out):
   handle_in = open(path_in, mode = 'r')
   source = handle_in.read()
   handle_in.close()
   document = STEM.Document({"source": source})
   document.parse()
   sink = document.write()
   handle_out = open(path_out, mode = 'w')
   handle_out.write(sink)
   handle_out.close()
